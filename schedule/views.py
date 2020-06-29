from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from datetime import datetime

from immunotherapy.models import Immunotherapy
from .models import Appointment
from .forms import AppointmentForm

from patient.models import Patient


class ScheduleView(LoginRequiredMixin, TemplateView):
    template_name = 'schedule.html'

    def get_context_data(self, **kwargs):
        context = super(ScheduleView, self).get_context_data(**kwargs)
        context["schedulePage"] = "active"
        return context


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'appointment/form.html'
    model = Appointment
    form_class = AppointmentForm

    def get_parameters(self):
        return {
            'start': self.request.GET.get('start'),
            'end': self.request.GET.get('end'),
            'patient': self.request.GET.get('patient')
        }

    def get_context_data(self, **kwargs):
        context = super(AppointmentCreateView, self).get_context_data(**kwargs)
        context["schedulePage"] = "active"
        patient_id = self.get_parameters()['patient']
        if patient_id:
            patient = Patient.objects.get(id=patient_id)
            context["patient"] = patient
        context["start"] = self.get_parameters()['start']
        context["end"] = self.get_parameters()['end']
        return context

    def get_initial(self):
        initial = super(AppointmentCreateView, self).get_initial()
        initial = initial.copy()
        start = self.get_parameters()['start']
        end = self.get_parameters()['end']
        if start and end:
            start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S.%fZ")
            end = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S.%fZ")
            initial['date'] = start.date().strftime('%d/%m/%Y')
            initial['start_hour'] = start.time()
            initial['end_hour'] = end.time()
        return initial

    def form_valid(self, form):
        date = form.cleaned_data['date']
        start_hour = form.cleaned_data['start_hour']
        end_hour = form.cleaned_data['end_hour']

        start_date = datetime.strptime("{} {}".format(date, start_hour), "%Y-%m-%d %H:%M:%S")
        end_date = datetime.strptime("{} {}".format(date, end_hour), "%Y-%m-%d %H:%M:%S")

        form.instance.start = start_date
        form.instance.end = end_date

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('schedule')


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'appointment/form.html'
    model = Appointment
    form_class = AppointmentForm

    def get_context_data(self, **kwargs):
        context = super(AppointmentUpdateView, self).get_context_data(**kwargs)
        context["schedulePage"] = "active"
        return context

    def get_initial(self):
        appointment = Appointment.objects.get(pk=self.object.pk)
        initial = super(AppointmentUpdateView, self).get_initial()
        initial = initial.copy()
        start = appointment.start
        end = appointment.end
        initial['date'] = start.date().strftime('%d/%m/%Y')
        initial['start_hour'] = start.time()
        initial['end_hour'] = end.time()
        return initial

    def get_success_url(self):
        return reverse('schedule')


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment

    def get_success_url(self):
        return reverse('schedule')


class AppointmentCreateModal(LoginRequiredMixin, CreateView):
    template_name = 'appointment/form-modal.html'
    model = Appointment
    form_class = AppointmentForm

    def get_immunotherapy(self):
        immunotherapy_id = self.kwargs['immunotherapy_id']
        return Immunotherapy.objects.get(pk=immunotherapy_id)

    def get_initial(self):
        initial = super(AppointmentCreateModal, self).get_initial()
        initial = initial.copy()
        initial['patient'] = self.get_immunotherapy().patient
        return initial

    def get_context_data(self, **kwargs):
        context = super(AppointmentCreateModal, self).get_context_data(**kwargs)
        context["immunotherapy"] = self.get_immunotherapy()
        return context

    def form_valid(self, form):
        date = form.cleaned_data['date']
        start_hour = form.cleaned_data['start_hour']
        end_hour = form.cleaned_data['end_hour']

        start_date = datetime.strptime("{} {}".format(date, start_hour), "%Y-%m-%d %H:%M:%S")
        end_date = datetime.strptime("{} {}".format(date, end_hour), "%Y-%m-%d %H:%M:%S")

        form.instance.start = start_date
        form.instance.end = end_date

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('immunotherapy_detail', kwargs={'pk': self.get_immunotherapy().id})
