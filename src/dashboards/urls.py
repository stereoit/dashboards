from dashboards.api import KPIResource, KPIValueResource, UserResource
from dashboards.api import ColorResource, ColorPaletteResource, GraphResource
from django.conf.urls import patterns, include, url
from dashboards.graphs.views import update_kpis
from dashboards.api import v1_api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dashboards.views.home', name='home'),
    # url(r'^dashboards/', include('dashboards.foo.urls')),
    url('update-kpis/', update_kpis, name='update-kpis'),
    url(r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
