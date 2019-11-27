from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(permanent=False, url='/agenda/'), name='index'),
    path('agenda/', include('schedule.urls')),
    path('imunoterapia/', include('immunotherapy.urls')),
    path('pacientes/', include('patient.urls')),
    path('farmacia/', include('pharmacy.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
