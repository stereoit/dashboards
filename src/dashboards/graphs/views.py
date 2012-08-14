import logging
from datetime import datetime, timedelta
from django.utils import timezone, simplejson
from dashboards.graphs.models import KPI, KPIValue
from django.http import HttpResponse

logger = logging.getLogger(__name__)

DEFAULT_NEXT_POLL = 300 # 5 minutes

def update_kpis(request):
    """Update all KPIs to current time"""
    json_response = {'updated_kpis':0, 'kpis': [] }
    updated_kpis = 0
    now = timezone.now()
    next_poll = timedelta(seconds=DEFAULT_NEXT_POLL)

    for kpi in KPI.objects.all():
        logger.debug('KPI "{0}"'.format(kpi.name))
        granularity = timedelta(seconds=kpi.granularity)
        generated_values = 0
        logger.debug('granularity {0}'.format(granularity))
        latest = None
        try:
            latest = kpi.values.latest()
            logger.debug('latest {0} now {1}'.format(latest.timestamp, now))
            interval = (now - latest.timestamp)
            missing_intervals = (interval.days * 3600 * 24 + interval.seconds) \
                                        / kpi.granularity
            if missing_intervals > kpi.history:
                missing_intervals = kpi.history
                latest = None
        except KPIValue.DoesNotExist:
            missing_intervals = kpi.history

        logger.debug('missing intervals {0}'.format(missing_intervals))

        if missing_intervals:
            updated_kpis += 1
            if latest:
                timestamp = latest.timestamp + timedelta(seconds=kpi.granularity)
            else:
                timestamp = now - timedelta(seconds=kpi.granularity * missing_intervals)
            for interval in range(0, missing_intervals):
                for value in kpi.generator.generate_value():
                    kpi.values.create(value=value, timestamp=timestamp)
                    generated_values += 1
                timestamp += timedelta(seconds=kpi.granularity)

            logger.debug('timestamp {0} granularity {1}'.format(timestamp, granularity))

        poll = kpi.values.latest().timestamp + granularity - now
        logger.debug('poll {0} next_poll {1}'.format(poll, next_poll))

        if next_poll > poll:
            next_poll = poll

        json_response['kpis'].append({
            'kpi': kpi.name,
            'missing_intervals': missing_intervals,
            'generated_values' : generated_values,
            })


    json_response['next_poll'] = (next_poll.days * 3600 * 24 + next_poll.seconds)
    json_response['updated_kpis'] = updated_kpis

    return HttpResponse(simplejson.dumps(json_response),
            mimetype='application/json')
