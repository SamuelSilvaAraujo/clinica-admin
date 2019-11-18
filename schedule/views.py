from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ScheduleView(LoginRequiredMixin, TemplateView):
    template_name = 'schedule.html'

    def get_context_data(self, **kwargs):
        context = super(ScheduleView, self).get_context_data(**kwargs)
        context["schedulePage"] = "active"
        return context
