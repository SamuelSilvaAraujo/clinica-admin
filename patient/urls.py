from django.urls import path, include
from .views import PatientListView, PatientCreateView, PatientUpdateView, PatientDeleteView, PatientDetailView
from .ajax import get_patients_ajax

urlpatterns = [
    path('', PatientListView.as_view(), name='patients'),
    path('criar/', PatientCreateView.as_view(), name='patient_create'),
    path('<int:pk>/', include([
        path('atualizar/', PatientUpdateView.as_view(), name='patient_update'),
        path('excluir/', PatientDeleteView.as_view(), name='patient_delete'),
        path('perfil/', PatientDetailView.as_view(), name='patient_detail'),
    ])),
    path('ajax/list/', get_patients_ajax, name='ajax_patients'),
]
