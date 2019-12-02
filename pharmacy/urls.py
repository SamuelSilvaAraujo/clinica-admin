from django.urls import path

from .views import *

urlpatterns = [
    path('remedios/', MedicineListView.as_view(), name='medicines'),
    path('remedio/criar/', MedicineCreateView.as_view(), name='medicine_create'),
    path('remedio/editar/<int:pk>/', MedicineUpdateView.as_view(), name='medicine_update'),
    path('remedio/excluir/<int:pk>/', MedicineDeleteView.as_view(), name='medicine_delete'),

    path('categorias/', MedicineCategoryListView.as_view(), name='categories'),
    path('categoria/criar/', MedicineCategoryCreateView.as_view(), name='category_create'),
    path('categoria/editar/<int:pk>/', MedicineCategoryUpdateView.as_view(), name='category_update'),
    path('categoria/excluir/<int:pk>/', MedicineCategoryDeleteView.as_view(), name='category_delete'),

    path('doencas/', IllnessListView.as_view(), name='illnesses'),
    path('doenca/criar/', IllnessCreateView.as_view(), name='illness_create'),
    path('doenca/editar/<int:pk>/', IllnessUpdateView.as_view(), name='illness_update'),
    path('doenca/excluir/<int:pk>/', IllnessDeleteView.as_view(), name='illness_delete'),

    path('estoque/', StockListView.as_view(), name='estoque')
]
