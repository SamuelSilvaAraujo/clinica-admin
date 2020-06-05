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
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=20, default=IN_PROGRESS)
    illness = models.ForeignKey(Illness, on_delete=models.SET_NULL, null=True, verbose_name='Doença')

    class Meta:
        ordering = ('-status', 'start_date', )

    def __str__(self):
        return "{} - {}".format(self.patient.name, self.medicine.name)

    def realized_applications(self):
        total = 0
        for bottle in self.bottle_set.all():
            total += bottle.application_set.count()
        return total

    def bottle_in_use(self):
        return self.bottle_set.filter(start_date__isnull=False, end_date__isnull=True).first()

    def last_bottle(self):
        return self.bottle_set.filter(start_date__isnull=False, end_date__isnull=False).last()

    def last_application(self):
        if self.bottle_set.first():
            return self.bottle_set.first().application_set.first()
        return None


class Bottle(models.Model):
    immunotherapy = models.ForeignKey(Immunotherapy, on_delete=models.CASCADE)
    number = models.IntegerField('Numero')
    start_date = models.DateField('Data de inicio')
    end_date = models.DateField('Data de Fim', null=True, blank=True)

    class Meta:
        ordering = ['start_date', 'end_date', ]

    def __str__(self):
        return "Imunotarepia: {} - Frasco: {}".format(self.immunotherapy.patient.name, self.number)


class Application(models.Model):
    bottle = models.ForeignKey(Bottle, on_delete=models.CASCADE)
    date = models.DateField('Data')
    applicator = models.CharField('Aplicador', max_length=50)
    dosage = models.CharField('Dosagem', max_length=10)

    class Meta:
        ordering = ('-date', )
