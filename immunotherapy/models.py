from django.db import models

from patient.models import Patient
from pharmacy.models import Medicine, Lot


class Immunotherapy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    total = models.IntegerField()


class Bottle(models.Model):
    USING = 'using'
    USED = 'used'

    STATUS_CHOICES = (
        (USING, 'Usando'),
        (USED, 'usado')
    )

    immunotherapy = models.ForeignKey(Immunotherapy, on_delete=models.CASCADE)
    number = models.IntegerField()
    lote = models.ForeignKey(Lot, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)


class Application(models.Model):
    bottle = models.ForeignKey(Bottle, on_delete=models.CASCADE)
    date = models.DateField('Data')
    applicator = models.CharField('Aplicador', max_length=50)
    dosage = models.FloatField('Dosagem')
