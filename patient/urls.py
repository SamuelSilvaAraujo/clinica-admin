from django.urls import path, include
from .views import *
from .ajax import get_patients_ajax, get_cities_ajax

urlpatterns = [
    path('', PatientListView.as_view(), name='patients'),
    path('criar/', PatientCreateView.as_view(), name='patient_create'),
    path('<int:pk>/', include([
        path('atualizar/', PatientUpdateView.as_view(), name='patient_update'),
        path('excluir/', PatientDeleteView.as_view(), name='patient_delete'),
        path('perfil/', PatientDetailView.as_view(), name='patient_detail'),
        path('photo/', patient_photo_update, name='patient_photo'),
    ])),

    path('ajax/', include([
        path('patients/list/', get_patients_ajax, name='ajax_patients'),
        path('cities/', get_cities_ajax, name='get_cities_ajax'),
    ]))

]
