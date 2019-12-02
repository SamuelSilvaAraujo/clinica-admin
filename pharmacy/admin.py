from django.contrib import admin

from .models import MedicineCategory, Medicine, Lote, Illness

admin.site.register(Medicine)
admin.site.register(MedicineCategory)
admin.site.register(Lote)
admin.site.register(Illness)
