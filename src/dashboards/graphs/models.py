"""
"""
from random import randrange
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from colorful.fields import RGBColorField


class KPI(models.Model):
    """Model representing sets of values in a over a time period"""
    NAME_MAX_LENGTH = 200
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    history = models.IntegerField(default=100, help_text=_('How long to keep history.'))
    granularity = models.IntegerField(default=60, help_text=_('How often to update the KPI in seconds.'))
    generator = models.ForeignKey('KPIGenerator', help_text=_('Associated generator of values.'))

    class Meta:
        pass

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('kpi' )

class KPIValue(models.Model):
    """A value for each KPI"""
    kpi = models.ForeignKey('KPI', related_name='values')
    value = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['-timestamp']
        get_latest_by = 'timestamp'

    def __unicode__(self):
        return u'%s' % self.value

class ColorPalette(models.Model):
    """Provide various colors for the graphs"""
    name = models.CharField(max_length=100, blank=True)
    colors = models.ManyToManyField('Color')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('palettes')

class Color(models.Model):
    """Represents one color"""
    name = models.CharField(max_length=100, blank=False)
    color = RGBColorField()

    def __unicode__(self):
        return self.name

class Dashboard(models.Model):
    """Mapping between the user and the KPI"""
    kpi = models.ForeignKey('KPI')
    user = models.ForeignKey(User)
    palette = models.ForeignKey('ColorPalette', help_text=_(''))
    dashboard = models.CharField(max_length=100, help_text=_('Defines the type of graph.'))

    class Meta:
        pass

    def __unicode__(self):
        return u'%s %s %s' % (self.kpi, self.user, self.palette)

    @models.permalink
    def get_absolute_url(self):
        return ('graph' )

class KPIGenerator(models.Model):
    """Generator of values for each KPI"""
    name = models.CharField(max_length=100)
    paralel = models.PositiveIntegerField(default=1, help_text=_('How many values for one timestamp'))
    min_value = models.PositiveIntegerField(default=0, help_text=_('Minium generated value'))
    max_value = models.PositiveIntegerField(default=100, help_text=_('Minium generated value'))

    def generate_value(self):
        """Yield one value given the specs"""
        for i in xrange(0, randrange(1,self.paralel+1)):
            yield randrange(self.min_value, self.max_value)

    class Meta:
        pass

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('kpi-generator' )

