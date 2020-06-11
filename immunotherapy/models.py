from django.db import models

from patient.models import Patient
from pharmacy.models import Medicine, Lot, Illness


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
    total_bottles = models.IntegerField('Total de Frascos')
    total_applications = models.IntegerField('Total de Aplicações')
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=20, default=IN_PROGRESS)
    illness = models.ForeignKey(Illness, on_delete=models.SET_NULL, null=True, verbose_name='Doença')

    class Meta:
        ordering = ('-status', 'start_date', )

    def __str__(self):
        return "{} - {}".format(self.patient.name, self.medicine.name)

    def last_application(self):
        return self.application_set.last()


class Application(models.Model):
    immunotherapy = models.ForeignKey(Immunotherapy, on_delete=models.CASCADE)
    bottle_number = models.IntegerField("Frasco")
    application_number = models.IntegerField("Dose")
    date = models.DateField('Data')
    applicator = models.CharField('Aplicador', max_length=50)
    dosage = models.CharField('Dosagem', max_length=10)

    class Meta:
        ordering = ('application_number', )
