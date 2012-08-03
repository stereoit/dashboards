import logging
from datetime import datetime, timedelta
from django.utils import timezone, simplejson
from dashboards.graphs.models import KPI, KPIValue
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def update_kpis(request):
    """Update all KPIs to current time"""
    json_response = {'updated':0, 'kpis': [] }
    updated_kpis = 0
    now = timezone.now()
    for kpi in KPI.objects.all():
        delta = timedelta(seconds=kpi.granularity)
        try:
            latest = kpi.values.latest()
            interval = (now - latest.timestamp)
            missing_intervals = (interval.days * 3600 * 24 + interval.seconds) \
                                        / kpi.granularity
            if missing_intervals > kpi.history:
                missing_intervals = kpi.history
        except KPIValue.DoesNotExist:
            missing_intervals = kpi.history
        if missing_intervals:
            updated_kpis += 1
            last_value = now - delta * kpi.history
    json_response['kpis'].append({
        'kpi': kpi.name,
        'last_generated': last_value.strftime('%c'),
        'missing_intervals': missing_intervals
        })
    logger.debug('kpi {0} last generated at {1} missing_intervals \
            {2}'.format(kpi, last_value.strftime('%c'), missing_intervals))
    return HttpResponse(simplejson.dumps(json_response),
            mimetype='application/json')
