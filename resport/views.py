from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from immunotherapy.models import Immunotherapy


class ReportsView(LoginRequiredMixin, TemplateView):
    template_name = 'report/reports.html'

    def get_context_data(self, **kwargs):
        context = super(ReportsView, self).get_context_data(**kwargs)
        context["reportMenu"] = "active"
        return context


class ReportPatientView(LoginRequiredMixin, TemplateView):
    template_name = 'report/patient.html'

    def get_context_data(self, **kwargs):
        context = super(ReportPatientView, self).get_context_data(**kwargs)
        context["reportMenu"] = "active"
        context["status_choices"] = list(Immunotherapy.STATUS_CHOICES)
        return context


class ReportStockView(LoginRequiredMixin, TemplateView):
    template_name = 'report/stock.html'

    def get_context_data(self, **kwargs):
        context = super(ReportStockView, self).get_context_data(**kwargs)
        context["reportMenu"] = "active"
        return context
