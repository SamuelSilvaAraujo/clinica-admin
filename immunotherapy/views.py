from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from datetime import datetime

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

from patient.models import Patient
from .models import Immunotherapy, Application
from .forms import ImmunotherapyForm, ImmunotherapyFinisheForm, ApplicationForm, TagPdfForm


class ImmunotherapyListView(LoginRequiredMixin, ListView):
    model = Immunotherapy
    template_name = 'immunotherapy/list.html'

    def get_context_data(self, **kwargs):
        context = super(ImmunotherapyListView, self).get_context_data(**kwargs)
        context["immunotherapyPage"] = "active"
        return context


class ImmunotherapyCreateView(LoginRequiredMixin, CreateView):
    model = Immunotherapy
    template_name = 'immunotherapy/form.html'
    form_class = ImmunotherapyForm

    def get_parameters(self):
        return {
            'patient': self.request.GET.get('patient'),
        }

    def get_context_data(self, **kwargs):
        context = super(ImmunotherapyCreateView, self).get_context_data(**kwargs)
        context["immunotherapyPage"] = "active"
        patient_id = self.get_parameters()['patient']
        if patient_id:
            patient = Patient.objects.get(id=patient_id)
            context["patient"] = patient
        return context

    def get_initial(self):
        initial = super(ImmunotherapyCreateView, self).get_initial()
        initial = initial.copy()
        initial['start_date'] = datetime.today()
        return initial

    def get_success_url(self):
        return reverse('immunotherapy_detail', kwargs={'pk': self.object.id})


class ImmunotherapyUpdateView(LoginRequiredMixin, UpdateView):
    model = Immunotherapy
    template_name = 'immunotherapy/form.html'
    form_class = ImmunotherapyForm

    def get_context_data(self, **kwargs):
        context = super(ImmunotherapyUpdateView, self).get_context_data(**kwargs)
        context["immunotherapyPage"] = "active"
        return context

    def get_success_url(self):
        return reverse('immunotherapy_detail', kwargs={'pk': self.object.id})


class ImmunotherapyDeleteView(LoginRequiredMixin, DeleteView):
    model = Immunotherapy

    def get_success_url(self):
        return reverse('immunotherapy')


class ImmunotherapyFinisheView(LoginRequiredMixin, UpdateView):
    model = Immunotherapy
    template_name = 'immunotherapy/finishe-modal.html'
    form_class = ImmunotherapyFinisheForm

    def get_context_data(self, **kwargs):
        context = super(ImmunotherapyFinisheView, self).get_context_data(**kwargs)
        context["immunotherapy"] = self.object
        return context

    def get_initial(self):
        initial = super(ImmunotherapyFinisheView, self).get_initial()
        initial = initial.copy()
        initial['end_date'] = datetime.today()
        return initial

    def form_valid(self, form):
        form.instance.status = Immunotherapy.FINISHED
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('immunotherapy_detail', kwargs={'pk': self.object.id})


class ImmunotherapyDetailView(LoginRequiredMixin, DetailView):
    model = Immunotherapy
    template_name = 'immunotherapy/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ImmunotherapyDetailView, self).get_context_data(**kwargs)
        context["immunotherapyPage"] = "active"
        return context


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    template_name = 'application/form-modal.html'
    form_class = ApplicationForm

    def get_immunotherapy(self):
        immunotherapy_id = self.kwargs['immunotherapy_id']
        immunotherapy = Immunotherapy.objects.get(id=immunotherapy_id)
        return immunotherapy

    def get_context_data(self, **kwargs):
        context = super(ApplicationCreateView, self).get_context_data(**kwargs)
        context["immunotherapy"] = self.get_immunotherapy()
        return context

    def get_initial(self):
        initial = super(ApplicationCreateView, self).get_initial()
        initial = initial.copy()
        initial['date'] = datetime.today()
        immunotherapy = self.get_immunotherapy()
        last_application = immunotherapy.last_application()
        if not last_application:
            initial['bottle_number'] = 1
            initial['application_number'] = 1
        else:
            initial['application_number'] = last_application.application_number + 1
            if (last_application.application_number + 1) / immunotherapy.total_applications > last_application.bottle_number:
                initial['bottle_number'] = last_application.bottle_number + 1
            else:
                initial['bottle_number'] = last_application.bottle_number
        return initial

    def form_valid(self, form):
        form.instance.immunotherapy = self.get_immunotherapy()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('immunotherapy_detail', kwargs={'pk': self.get_immunotherapy().id})


class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Application
    template_name = 'application/form-modal.html'
    form_class = ApplicationForm

    def get_immunotherapy(self):
        immunotherapy_id = self.kwargs['immunotherapy_id']
        immunotherapy = Immunotherapy.objects.get(id=immunotherapy_id)
        return immunotherapy

    def get_context_data(self, **kwargs):
        context = super(ApplicationUpdateView, self).get_context_data(**kwargs)
        context["immunotherapy"] = "active"
        context["immunotherapy"] = self.get_immunotherapy()
        return context

    def get_success_url(self):
        return reverse('immunotherapy_detail', kwargs={'pk': self.get_immunotherapy().id})


class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Application

    def get_immunotherapy(self):
        immunotherapy_id = self.kwargs['immunotherapy_id']
        immunotherapy = Immunotherapy.objects.get(id=immunotherapy_id)
        return immunotherapy

    def get_success_url(self):
        return reverse('immunotherapy_detail', kwargs={'pk': self.get_immunotherapy().id})


class OpenTagModal(LoginRequiredMixin, FormView):
    form_class = TagPdfForm
    template_name = 'tag_modal.html'

    def __init__(self):
        super(OpenTagModal, self).__init__()
        self.patient = ""
        self.bottle_number = ""
        self.concentration = ""
        self.period = ""
        self.dimensions = ""

    def get_immunotherapy(self):
        immunotherapy_id = self.kwargs['immunotherapy_id']
        immunotherapy = Immunotherapy.objects.get(id=immunotherapy_id)
        return immunotherapy

    def get_context_data(self, **kwargs):
        context = super(OpenTagModal, self).get_context_data(**kwargs)
        context["immunotherapy"] = self.get_immunotherapy()
        return context

    def get_initial(self):
        initial = super(OpenTagModal, self).get_initial()
        initial = initial.copy()
        immunotherapy = self.get_immunotherapy()
        initial['patient'] = immunotherapy.patient.name
        last_application = immunotherapy.last_application()
        if not last_application:
            initial['bottle_number'] = 1
        else:
            initial['bottle_number'] = last_application.bottle_number
        return initial

    def form_valid(self, form):
        self.patient = form.cleaned_data['patient']
        self.bottle_number = form.cleaned_data['bottle_number']
        self.concentration = form.cleaned_data['concentration']
        self.period = form.cleaned_data['period']
        self.dimensions = form.cleaned_data['dimensions']
        return super(OpenTagModal, self).form_valid(form)

    def get_success_url(self):
        return "{}?patient={}&bottle_number={}&concentration={}&period={}&dimensions={}" \
            .format(reverse('create_pdf_tag'), self.patient, self.bottle_number, self.concentration, self.period, self.dimensions)


def create_pdf_tag(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="etiqueta.pdf"'

    p = canvas.Canvas(response)

    patient = request.GET.get('patient')
    bottle_number = request.GET.get('bottle_number')
    concentration = request.GET.get('concentration')
    period = request.GET.get('period')
    dimensions = request.GET.get('dimensions')

    if dimensions == '3x2':
        p.setPageSize((3 * cm, 2 * cm))
        p.setFontSize(4)
        p.drawString(3, 43, patient)
        p.drawString(3, 36, "{}° frasco {}".format(bottle_number, concentration))
        p.drawString(3, 29, period)
    elif dimensions == '10x4':
        p.setPageSize((10 * cm, 4 * cm))
        p.setFontSize(14)
        p.drawString(5, 85, patient)
        p.drawString(5, 58, "{}° frasco {}".format(bottle_number, concentration))
        p.drawString(5, 32, period)
    p.showPage()
    p.save()
    return response
