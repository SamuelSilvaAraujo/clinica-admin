from django.db import models
from datetime import date

from django.db.models import Sum

from patient.models import Patient


class Spirometry(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Paciente")
    date = models.DateField("Data")

    def __str__(self):
        return "{} - {}".format(self.patient.name, date.strftime(self.date, "%d/%m/%Y"))


class Material(models.Model):
    name = models.CharField("Nome", max_length=50)

    def __str__(self):
        return self.name

    def amount_in_stock(self):
        return self.stock_set.aggregate(total=Sum('amount')).get('total') - Spirometry.objects.count() or 0


class Stock(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Material")
    date = models.DateField("Data")
    amount = models.IntegerField("Quantidade")

    def __str__(self):
        return "{} - {}".format(self.material.name, date.strftime(self.date, "%d/%m/%Y"))
