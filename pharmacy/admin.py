from django.contrib import admin

from .models import MedicineCategory, Medicine, Lot, Illness

admin.site.register(Medicine)
admin.site.register(MedicineCategory)
admin.site.register(Lot)
admin.site.register(Illness)
