import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q, Count, Value, IntegerField
from django.core.serializers.json import DjangoJSONEncoder

from datetime import datetime

from immunotherapy.models import Immunotherapy
from pharmacy.models import Lot


@login_required()
def report_patients_ajax(request):
    if request.is_ajax():
        date_range = request.GET.get('date_range')
        dates_str = date_range.split(' - ')

        status = request.GET.get('status')

        q_objects = Q()

        if dates_str:
            start, end = datetime.strptime(dates_str[0], '%d/%m/%Y'), datetime.strptime(dates_str[1], '%d/%m/%Y')
            q_objects.add(Q(start_date__gte=start, start_date__lte=end), Q.AND)

        if status and status != 'all':
            q_objects.add(Q(status=status), Q.AND)

        immunotherapies = Immunotherapy.objects.filter(q_objects) \
            .order_by('patient') \
            .annotate(bottles_used=Count('bottle')) \
            .values('patient__name', 'start_date', 'end_date', 'illness__name',
                    'medicine__name', 'bottles_used')

        data = json.dumps({'aaData': list(immunotherapies)}, cls=DjangoJSONEncoder)
    else:
        data = 'fail'

    return HttpResponse(data, 'application/json')


@login_required()
def report_stock_ajax(request):
    if request.is_ajax():
        date_range = request.GET.get('date_range')
        dates_str = date_range.split(' - ')

        q_objects = Q()

        if dates_str:
            start, end = datetime.strptime(dates_str[0], '%d/%m/%Y'), datetime.strptime(dates_str[1], '%d/%m/%Y')
            q_objects.add(Q(entry_date__gte=start, entry_date__lte=end), Q.AND)

        lots = Lot.objects.filter(q_objects) \
            .order_by('medicine') \
            .values('medicine__name', 'medicine__supplier', 'entry_date', 'shelf_life_date', 'amount')

        data = json.dumps({'aaData': list(lots)}, cls=DjangoJSONEncoder)
    else:
        data = 'fail'

    return HttpResponse(data, 'application/json')
