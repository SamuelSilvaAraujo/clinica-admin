from django.urls import path

from .views import MedicineListView

urlpatterns = [
    path('remedios/', MedicineListView.as_view(), name='remedios'),
]
