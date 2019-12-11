from django.db import models

from patient.models import Patient
from pharmacy.models import Medicine, Lot


class Bottle(models.Model):
    bottle_number = models.IntegerField('Numero')
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, verbose_name='Lote')

    def __str__(self):
        return "{}".format(self.bottle_number)


class Application(models.Model):
    bottle = models.ForeignKey(Bottle, on_delete=models.CASCADE)
    date = models.DateField('Data')
    applicator = models.CharField('Aplicador', max_length=50)
    dosage = models.FloatField('Dosagem')

    class Meta:
        ordering = ('-date',)


class Immunotherapy(models.Model):
    FINISHED = 'finished'
    IN_PROGRESS = 'in-progress'

    STATUS_CHOICES = (
        (FINISHED, 'Finalizado'),
        (IN_PROGRESS, 'Em Andamento')
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='Remédio')
    start_date = models.DateField('Data de Inicio')
    end_date = models.DateField('Data de Fim', null=True, blank=True)
    total_applications = models.IntegerField('Total de aplicações')
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=20, default=IN_PROGRESS)
    bottle = models.OneToOneField(Bottle, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('status', 'start_date', )

    def __str__(self):
        return "{} - {}".format(self.patient.name, self.medicine.name)

    def realized_applications(self):
        if self.bottle:
            return self.bottle.application_set.count()
        return 0

    def last_application(self):
        return self.bottle.application_set.first()
