from django.db import models

from patient.models import Patient
from pharmacy.models import Medicine, Lot


class Immunotherapy(models.Model):
    FINISHED = 'finished'
    IN_PROGRESS = 'in-progress'

    STATUS_CHOICES = (
        (FINISHED, 'Finalizado'),
        (IN_PROGRESS, 'Em Andamento')
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    start_date = models.DateField()
    total_applications = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)


class Bottle(models.Model):
    IN_USE = 'in-use'
    USED = 'used'

    STATUS_CHOICES = (
        (IN_USE, 'Em uso'),
        (USED, 'usado')
    )

    immunotherapy = models.ForeignKey(Immunotherapy, on_delete=models.CASCADE)
    bottle_number = models.IntegerField()
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)


class Application(models.Model):
    bottle = models.ForeignKey(Bottle, on_delete=models.CASCADE)
    date = models.DateField('Data')
    applicator = models.CharField('Aplicador', max_length=50)
    dosage = models.FloatField('Dosagem')
