from django.urls import path, include

from .views import *
from .ajax import *

urlpatterns = [
    path('', ReportsView.as_view(), name='reports'),
    path('imunoterapia/', ReportImmunotherapyView.as_view(), name='report_immunotherapy'),
    path('espirometria/', ReportSpirometryView.as_view(), name='report_spirometry'),
    path('estoque/', ReportStockView.as_view(), name='report_stock'),

    path('imunoterapia/ajax/', report_immunotherapy_ajax, name='report_imunoterapia_ajax'),
    path('espirometria/ajax/', report_spirometry_ajax, name='report_spirometry_ajax'),
    path('stock/ajax/', report_stock_ajax, name='report_stock_ajax'),
]
