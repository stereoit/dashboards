import logging
from datetime import datetime, timedelta
from django.utils import timezone, simplejson
from dashboards.graphs.models import KPI, KPIValue
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def update_kpis(request):
    """Update all KPIs to current time"""
    json_response = []
    now = timezone.now()
    for kpi in KPI.objects.all():
        delta = timedelta(seconds=kpi.granularity)
        try:
            latest = kpi.values.latest()
            difference = (now - latest.timestamp)
            missing_intervals = (difference.days * 3600 * 24 + difference.seconds) / kpi.granularity
            if missing_intervals > kpi.history:
                missing_intervals = kpi.history
        except KPIValue.DoesNotExist:
            missing_intervals = kpi.history
        last_value = now - delta * kpi.history
        json_response.append({
            'kpi': kpi.name,
            'last_generated': last_value.strftime('%c'), 
            'missing_intervals': missing_intervals 
        })
        logger.debug('kpi {0} last generated at {1} missing_intervals {2}'.format(kpi, last_value.strftime('%c'), missing_intervals))
    return HttpResponse(simplejson.dumps(json_response), mimetype='application/json')
    #return HttpResponse("<html><body>Updated</body></html>")
