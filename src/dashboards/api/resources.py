import json
from django.conf.urls import url
from django.http import HttpResponse
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash
from django.contrib.auth.models import User
from dashboards.graphs.models import Dashboard, KPI, KPIValue, \
    ColorPalette, Color, KPIGenerator
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


class KPIValueResource(ModelResource):
    kpi = fields.ForeignKey('dashboards.api.KPIResource', 'kpi')

    class Meta:
        queryset = KPIValue.objects.all()
        resource_name = 'value'
        excludes = ['id']

class KPIResource(ModelResource):
    #values = fields.ToManyField('dashboards.api.KPIValueResource', 'values', full=True)
    generator = fields.ToOneField('dashboards.api.KPIGeneratorResource', 'generator', full=True)

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/values%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_values'), name="api_get_values"),
                ]

    def get_values(self, request, **kwargs):
        try:
            obj = self.cached_obj_get(request=request, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this URI.")
        values_resource = KPIValueResource()
        return values_resource.get_list(request, kpi_id=obj.pk)

    class Meta:
        queryset = KPI.objects.all()
        resource_name = 'kpi'
        excludes = ['id']

class ColorPaletteResource(ModelResource):

    def dehydrate(self, bundle):
        bundle.data['colors'] =  [ (c.name, c.color) for c in bundle.obj.colors.all()]
        return bundle

    class Meta:
        queryset = ColorPalette.objects.all()

class ColorResource(ModelResource):
    class Meta:
        queryset = Color.objects.all()

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = [ 'email', 'first_name', 'last_name', 'username' ]

class KPIGeneratorResource(ModelResource):
    class Meta:
        queryset = KPIGenerator.objects.all()
        resource_name = 'generator'

class DashboardResource(ModelResource):
    kpi = fields.ForeignKey('dashboards.api.resources.KPIResource', 'kpi', full=True)
    user = fields.ForeignKey('dashboards.api.resources.UserResource', 'user', full=True)
    palette = fields.ForeignKey('dashboards.api.resources.ColorPaletteResource', 'palette', full=True)
    #values = fields.ToManyField('dashboards.api.resources.KPIValueResource',)

    def dehydrate(self, bundle):
        values = [(v.value,v.timestamp) for v in bundle.obj.kpi.values.all()]
        bundle.data['values'] = values
        return bundle

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/values%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_values'), name="api_get_values"),
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/all-values%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_all_values'), name="api_get_all_values"),
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/kpi%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_kpi'), name="api_get_kpi"),
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/palette%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_palette'), name="api_get_palette"),
                ]

    def get_all_values(self, request, **kwargs):
        try:
            obj = self.cached_obj_get(request=request, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this URI.")
        values = [{'value': '%.2f' % v.value, 'timestamp': '%s' % v.timestamp} for v in obj.kpi.values.all()]
        return HttpResponse(json.dumps(values, cls=DecimalEncoder), content_type='application/json')

    def get_values(self, request, **kwargs):
        try:
            obj = self.cached_obj_get(request=request, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this URI.")
        values_resource = KPIValueResource()
        return values_resource.get_list(request, kpi_id=obj.kpi)

    def get_kpi(self, request, **kwargs):
        try:
            obj = self.cached_obj_get(request=request, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this URI.")
        kpi_resource = KPIResource()
        return kpi_resource.get_detail(request, dashboard=obj.pk)

    def get_palette(self, request, **kwargs):
        try:
            obj = self.cached_obj_get(request=request, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this URI.")
        palette_resource = ColorPaletteResource()
        return palette_resource.get_detail(request, dashboard=obj.pk)
    class Meta:
        queryset = Dashboard.objects.all()

