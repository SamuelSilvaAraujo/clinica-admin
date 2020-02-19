from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(permanent=False, url='/agenda/'), name='index'),
    path('agenda/', include('schedule.urls')),
    path('imunoterapia/', include('immunotherapy.urls')),
    path('pacientes/', include('patient.urls')),
    path('farmacia/', include('pharmacy.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('espirometria/', include('spirometry.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
