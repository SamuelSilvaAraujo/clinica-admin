from django.db import models
from patient.models import Patient


class Appointment(models.Model):
    SCHEDULED = 'scheduled'
    CANCELLED = 'cancelled'
    DID_NOT_ATTEND = 'did-not-attend'
    ANSWERED = 'answered'

    STATUS_CHOICES = (
        (SCHEDULED, 'Agendado'),
        (CANCELLED, 'Cancelado'),
        (DID_NOT_ATTEND, 'Não Compareceu'),
        (ANSWERED, 'Atendido')
    )

    STATUS_COLORS = {
        SCHEDULED: '#4e73df',
        CANCELLED: '#e74a3b',
        DID_NOT_ATTEND: '#f6c23e',
        ANSWERED: '#1cc88a'
    }

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')
    start = models.DateTimeField('Hora de Início')
    end = models.DateTimeField('Hora de Fim')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=SCHEDULED)
    notes = models.TextField('Descrição')

    def __str__(self):
        return "{} | {}".format(self.patient.name, self.start.date())
