from django.urls import path

from .views import *

urlpatterns = [
    path('remedios/', MedicineListView.as_view(), name='medicines'),

    path('categorias/', MedicineCategoryListView.as_view(), name='categories'),

    path('estoque/', StockListView.as_view(), name='estoque')
]
