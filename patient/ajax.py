import json

from django.conf import settings

from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.db.models import F

from .models import Patient


@login_required()
def get_patients_ajax(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        patients = Patient.objects.filter(name__icontains=q) \
            .values('id', 'name', ) \
            .annotate(label=F('name'))
        patients = list(patients)
        patients.append({'id': 'NEW_PATIENT', 'label': 'CADASTRAR PACIENTE', 'name': q})
        data = json.dumps(patients, cls=DjangoJSONEncoder)
    else:
        data = 'fail'
    return HttpResponse(data, 'application/json')


@login_required()
def get_cities_ajax(request):
    if request.is_ajax():
        state = request.GET.get('state')

        file_path = settings.BASE_DIR + '/static/files/estados-cidades.json'

        with open(file_path, "r", encoding='utf8') as read_file:
            data = json.load(read_file)

            states = data['estados']

            cities = []

            for s in states:
                if s['sigla'] == state:
                    cities = s['cidades']

        data = json.dumps(cities)
    else:
        data = 'fail'
    return HttpResponse(data, 'application/json')
