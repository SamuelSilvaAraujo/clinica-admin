from django.urls import path
from .views import ScheduleView, AppointmentCreateView

urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule'),
    path('agenda/novoevento/', AppointmentCreateView.as_view(), name='appointment_create'),
]
