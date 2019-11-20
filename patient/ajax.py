import json

from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.db.models import F

from .models import Patient


@login_required()
def get_patients_ajax(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        patients = Patient.objects.filter(name__contains=q) \
            .values('id', 'name', )\
            .annotate(label=F('name'))
        patients = list(patients)
        patients.append({'id': 'NEW_PATIENT', 'label': 'CADASTRAR PACIENTE', 'name': q})
        data = json.dumps(patients, cls=DjangoJSONEncoder)
    else:
        data = 'fail'
    return HttpResponse(data, 'application/json')