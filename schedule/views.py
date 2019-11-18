from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ScheduleView(LoginRequiredMixin, TemplateView):
    template_name = 'schedule.html'
