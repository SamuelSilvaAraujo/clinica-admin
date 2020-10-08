from django.urls import path, include
from .views import *
from .ajax import get_appointments_ajax, set_appointment_status_ajax

urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule'),
    path('agendamento/', include([
        path('criar/', AppointmentCreateView.as_view(), name='appointment_create'),
        path('<int:pk>/', include([
            path('atualizar/', AppointmentUpdateView.as_view(), name='appointment_update'),
            path('excluir/', AppointmentDeleteView.as_view(), name='appointment_delete'),
        ])),
    ])),

    path('agendamentos/ajax/', get_appointments_ajax, name='appointments_ajax'),
    path('agendamento/set/status/ajax/', set_appointment_status_ajax, name='set_appointment_status_ajax'),
]
