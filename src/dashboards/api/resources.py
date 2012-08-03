from tastypie import fields
from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from dashboards.graphs.models import Graph, KPI, KPIValue
from dashboards.graphs.models import ColorPalette, Color


class GraphResource(ModelResource):
    class Meta:
        queryset = Graph.objects.all()

class KPIResource(ModelResource):
    values = fields.ToManyField('dashboards.api.KPIValueResource', 'values', full=True)

    class Meta:
        queryset = KPI.objects.all()
        resource_name = 'kpi'
        excludes = ['id']

class KPIValueResource(ModelResource):
    kpi = fields.ForeignKey(KPIResource, 'kpi')

    class Meta:
        queryset = KPIValue.objects.all()
        resource_name = 'value'
        excludes = ['id']

class ColorPaletteResource(ModelResource):
    class Meta:
        queryset = ColorPalette.objects.all()

class ColorResource(ModelResource):
    class Meta:
        queryset = Color.objects.all()

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()

