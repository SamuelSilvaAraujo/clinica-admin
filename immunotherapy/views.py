from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import datetime

from patient.models import Patient
from .models import Immunotherapy, Bottle, Application
from .forms import ImmunotherapyForm, BottleForm, ApplicationForm, ImmunotherapyFinisheForm


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


class BottleCreateView(LoginRequiredMixin, CreateView):
    model = Bottle
    template_name = 'bottle/form-modal.html'
    form_class = BottleForm

    def get_immunotherapy(self):
        immunotherapy_id = self.kwargs['immunotherapy_id']
        immunotherapy = Immunotherapy.objects.get(id=immunotherapy_id)
        return immunotherapy

    def get_context_data(self, **kwargs):
        context = super(BottleCreateView, self).get_context_data(**kwargs)
        context["immunotherapy"] = self.get_immunotherapy()
        return context

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(BottleCreateView, self).get_form_kwargs()
        form_kwargs["immunotherapy"] = self.get_immunotherapy()
        return form_kwargs

    def form_valid(self, form):
        response = super(BottleCreateView, self).form_valid(form)
        immunotherapy = self.get_immunotherapy()
        immunotherapy.bottle = self.object
        immunotherapy.save()
        return response

    def get_success_url(self):
        return reverse('immunotherapy_detail', kwargs={'pk': self.kwargs['immunotherapy_id']})


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
        return initial

    def form_valid(self, form):
        form.instance.bottle = self.get_immunotherapy().bottle
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('immunotherapy_detail', kwargs={'pk': self.get_immunotherapy().id})
