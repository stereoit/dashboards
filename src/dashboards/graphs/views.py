import logging
from datetime import datetime, timedelta
from django.utils import timezone, simplejson
from dashboards.graphs.models import KPI, KPIValue
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def update_kpis(request):
    """Update all KPIs to current time"""
    json_response = {'updated_kpis':0, 'kpis': [] }
    updated_kpis = 0
    next_poll = None
    now = timezone.now()

    for kpi in KPI.objects.all():
        logger.debug('KPI "{0}"'.format(kpi.name))
        delta = timedelta(seconds=kpi.granularity)
        generated_values = 0
        logger.debug('delta {0}'.format(delta))
        logger.debug('now {0}'.format(now))
        try:
            latest = kpi.values.latest()
            logger.debug('latest {0} now {1}'.format(latest.timestamp, now))
            interval = (now - latest.timestamp)
            missing_intervals = (interval.days * 3600 * 24 + interval.seconds) \
                                        / kpi.granularity
            if missing_intervals > kpi.history:
                missing_intervals = kpi.history
        except KPIValue.DoesNotExist:
            missing_intervals = kpi.history

        logger.debug('missing intervals {0}'.format(missing_intervals))
        if missing_intervals:
            updated_kpis += 1
            last_value = now - delta * kpi.history
            timestamp = now - timedelta(seconds=kpi.granularity * missing_intervals)
            logger.debug('last value {0}'.format(last_value))
            for interval in range(0, missing_intervals):
                for value in kpi.generator.generate_value():
                    kpi.values.create(value=value, timestamp=timestamp)
                    generated_values += 1
                    logger.debug('timestamp {0}'.format(timestamp))
                timestamp += timedelta(seconds=kpi.granularity)
            poll = timestamp+delta
            logger.debug('poll {0} next_poll {1}'.format(poll, next_poll))

            if not next_poll or next_poll > poll:
                next_poll = poll

        json_response['kpis'].append({
            'kpi': kpi.name,
            'last_generated': last_value.strftime('%c'),
            'missing_intervals': missing_intervals,
            'generated_values' : generated_values,
            })

        logger.debug('kpi {0} last generated at {1} missing_intervals \
                {2}'.format(kpi, last_value.strftime('%c'), missing_intervals))
    if next_poll:
        next_poll = next_poll - now
        json_response['next_poll'] = (next_poll.days * 3600 * 24 + next_poll.seconds)
    else:
        json_response['next_poll'] = 300

    json_response['updated_kpis'] = updated_kpis

    return HttpResponse(simplejson.dumps(json_response),
            mimetype='application/json')
