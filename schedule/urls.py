from django.urls import path
from .views import ScheduleView, AppointmentCreateView, AppointmentUpdateView
from .ajax import get_appointments_ajax

urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule'),
    path('create/agendamento/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('update/agendamento/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('delete/agendamento/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment_delete'),

    path('agendamentos/ajax/', get_appointments_ajax, name='appointments_ajax')
]
