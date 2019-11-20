from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

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
    template_name = 'appointment/create.html'
    model = Appointment
    form_class = AppointmentForm

    def get_context_data(self, **kwargs):
        context = super(AppointmentCreateView, self).get_context_data(**kwargs)
        context["schedulePage"] = "active"
        patient_id = self.request.GET.get('patient_id')
        if patient_id:
            patient = Patient.objects.get(id=patient_id)
            context["patient"] = patient
        return context
