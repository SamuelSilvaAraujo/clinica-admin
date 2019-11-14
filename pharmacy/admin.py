from django.contrib import admin

from .models import MedicineCategory, MedicineApplication, Medicine, Lote

admin.site.register(Medicine)
admin.site.register(MedicineCategory)
admin.site.register(MedicineApplication)
admin.site.register(Lote)
