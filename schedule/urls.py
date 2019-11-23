from django.urls import path
from .views import ScheduleView, AppointmentCreateView
from .ajax import get_appointments_ajax

urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule'),
    path('agenda/create/agendamento/', AppointmentCreateView.as_view(), name='appointment_create'),

    path('agendamentos/ajax/', get_appointments_ajax, name='appointments_ajax')
]
