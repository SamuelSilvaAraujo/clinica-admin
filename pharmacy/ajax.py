import json

from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.db.models import F

from .models import Medicine


@login_required()
def get_medicines_ajax(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        medicines = Medicine.objects.filter(name__icontains=q) \
            .values('id', 'name', )\
            .annotate(label=F('name'))
        medicines = list(medicines)
        medicines.append({'id': 'NEW_MEDICINE', 'label': 'CADASTRAR MEDICAMENTO', 'name': q})
        data = json.dumps(medicines, cls=DjangoJSONEncoder)
    else:
        data = 'fail'
    return HttpResponse(data, 'application/json')
