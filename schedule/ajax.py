import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import F

from datetime import datetime

from .models import Appointment


@login_required()
def get_appointments_ajax(request):
    start = request.GET.get('start')
    end = request.GET.get('end')

    start = start[:-3] + start[-2:]
    end = end[:-3] + end[-2:]
    start = datetime.strptime(start, '%Y-%m-%dT%H:%M:%S%z')
    end = datetime.strptime(end, '%Y-%m-%dT%H:%M:%S%z')

    appointments = Appointment.objects \
        .filter(start__date__gte=start, end__date__lte=end) \
        .values('id', 'patient__name', 'patient__id', 'start', 'end', 'notes', 'status') \
        .annotate(title=F('patient__name'), resourceId=F('patient__id'))

    return JsonResponse(list(appointments), safe=False)
