from django.urls import path
from .views import ScheduleView, AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView
from .ajax import get_appointments_ajax, set_appointment_status_ajax

urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule'),
    path('criar/agendamento/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('atualizar/agendamento/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('excluir/agendamento/<int:pk>/', AppointmentDeleteView.as_view(), name='appointment_delete'),

    path('agendamentos/ajax/', get_appointments_ajax, name='appointments_ajax'),
    path('agendamento/set/status/ajax/', set_appointment_status_ajax, name='set_appointment_status_ajax'),
]
