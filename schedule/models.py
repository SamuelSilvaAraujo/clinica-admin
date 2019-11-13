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

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    start = models.DateTimeField('Hora de Início')
    end = models.DateTimeField('Hora de Fim')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
