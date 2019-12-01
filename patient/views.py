from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Patient
from .forms import PatientForm, PhotoForm


class PatientListView(LoginRequiredMixin, ListView):
    template_name = 'patient/list.html'
    model = Patient

    def get_context_data(self, **kwargs):
        context = super(PatientListView, self).get_context_data(**kwargs)
        context["patientsPage"] = "active"
        return context


class PatientCreateView(LoginRequiredMixin, CreateView):
    template_name = 'patient/form.html'
    model = Patient
    form_class = PatientForm

    def get_context_data(self, **kwargs):
        context = super(PatientCreateView, self).get_context_data(**kwargs)
        context["patientsPage"] = "active"
        return context

    def get_initial(self):
        initial = super(PatientCreateView, self).get_initial()
        initial = initial.copy()
        patient_name = self.request.GET.get('patient_name')
        if patient_name:
            initial['name'] = patient_name
        return initial

    def get_success_url(self):
        patient_name = self.request.GET.get('patient_name')
        if patient_name:
            return '{}?patient_id={}'.format(reverse('appointment_create'), self.object.id)
        return reverse('patients')


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'patient/form.html'
    model = Patient
    form_class = PatientForm

    def get_context_data(self, **kwargs):
        context = super(PatientUpdateView, self).get_context_data(**kwargs)
        context["patientsPage"] = "active"
        return context

    def get_success_url(self):
        return reverse('patients')


class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient

    def get_success_url(self):
        return reverse('patients')


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patient/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        context["patientsPage"] = "active"
        return context


class PatientPhotoUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = 'patient/detail.html'
    form_class = PhotoForm

    def get_success_url(self):
        return reverse('patient_detail', kwargs={'pk': self.object.id})
