from django.urls import path

from .views import *

urlpatterns = [

    path('', ImmunotherapyListView.as_view(), name='immunotherapy'),
    path('criar/', ImmunotherapyCreateView.as_view(), name='immunotherapy_create'),
    path('editar/<int:pk>/', ImmunotherapyUpdateView.as_view(), name='immunotherapy_update'),
    path('excluir/<int:pk>/', ImmunotherapyDeleteView.as_view(), name='immunotherapy_delete'),
    path('detalhe/<int:pk>/', ImmunotherapyDetailView.as_view(), name='immunotherapy_detail'),

]
