from django.urls import path
from .views import PatientListView, PatientCreateView, PatientUpdateView, PatientDeleteView

urlpatterns = [
    path('', PatientListView.as_view(), name='patients'),
    path('create/', PatientCreateView.as_view(), name='patient_create'),
    path('update/<int:pk>/', PatientUpdateView.as_view(), name='patient_update'),
    path('delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),
]
