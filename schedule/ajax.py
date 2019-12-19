from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import get_object_or_404

from datetime import datetime

from .models import Appointment


@login_required()
def get_appointments_ajax(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    start = datetime.strptime(start, '%Y-%m-%dT%H:%M:%S')
    end = datetime.strptime(end, '%Y-%m-%dT%H:%M:%S')

    appointments = Appointment.objects \
        .filter(start__date__gte=start, end__date__lte=end) \
        .values('id', 'patient__name', 'patient__id', 'start', 'end', 'notes', 'status') \
        .annotate(title=F('patient__name'), resourceId=F('patient__id'))

    for ap in appointments:
        ap['bgcolor'] = Appointment.STATUS_COLORS[ap['status']]
        ap['start'] = ap['start'].astimezone()
        ap['end'] = ap['end'].astimezone()

    return JsonResponse(list(appointments), safe=False)


@login_required()
def set_appointment_status_ajax(request):
    if request.is_ajax():
        appointment_id = request.POST.get('appointment_id')
        status = request.POST.get('status')

        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.status = status
        appointment.save()

        data = {'status': 'success'}
    else:
        data = {'status': 'fail'}
    return JsonResponse(data, safe=False)
