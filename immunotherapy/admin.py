from django.contrib import admin

from .models import Immunotherapy, Bottle, Application

admin.site.register(Immunotherapy)
admin.site.register(Bottle)
admin.site.register(Application)
