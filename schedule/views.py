from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from datetime import datetime

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
