from django.urls import path, include

from .views import *
from .ajax import *

urlpatterns = [
    path('', ReportsView.as_view(), name='reports'),
    path('paciente/', ReportPatientView.as_view(), name='report_patient'),
    path('estoque/', ReportStockView.as_view(), name='report_stock'),

    path('report_patients_ajax/', report_patients_ajax, name='report_patients_ajax'),
    path('report_stock_ajax/', report_stock_ajax, name='report_stock_ajax'),
]
