from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from immunotherapy.models import Immunotherapy


class ReportsView(LoginRequiredMixin, TemplateView):
    template_name = 'report/reports.html'

    def get_context_data(self, **kwargs):
        context = super(ReportsView, self).get_context_data(**kwargs)
        context["reportMenu"] = "active"
        return context


class ReportImmunotherapyView(LoginRequiredMixin, TemplateView):
    template_name = 'report/immunotherapy.html'

    def get_context_data(self, **kwargs):
        context = super(ReportImmunotherapyView, self).get_context_data(**kwargs)
        context["reportMenu"] = "active"
        context["status_choices"] = list(Immunotherapy.STATUS_CHOICES)
        return context


class ReportSpirometryView(LoginRequiredMixin, TemplateView):
    template_name = 'report/spirometry.html'

    def get_context_data(self, **kwargs):
        context = super(ReportSpirometryView, self).get_context_data(**kwargs)
        context["reportMenu"] = "active"
        return context


class ReportStockView(LoginRequiredMixin, TemplateView):
    template_name = 'report/stock.html'

    def get_context_data(self, **kwargs):
        context = super(ReportStockView, self).get_context_data(**kwargs)
        context["reportMenu"] = "active"
        return context
