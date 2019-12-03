from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

import re
import base64
from io import BytesIO
from PIL import Image
from django.core.files import File

from .models import Patient
from .forms import PatientForm


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


@login_required()
def patient_photo_update(request, pk):
    patient = Patient.objects.get(pk=pk)

    if request.POST:
        image_data = request.POST['image_data']
        image_data = re.sub("^data:image/png;base64,", "", image_data)
        image_data = base64.b64decode(image_data)
        image_data = BytesIO(image_data)
        im = Image.open(image_data)
        im = im.convert("RGB")

        blob = BytesIO()
        im.save(blob, 'JPEG')
        patient.photo.save('%s.jpg' % patient.id, File(blob), save=False)
        patient.save()
        return redirect('patient_detail', pk=patient.id)
    return render(request, 'patient/change-photo-modal.html', {'patient': patient})
