from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from dashboards.graphs.views import update_kpis

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dashboards.views.home', name='home'),
    # url(r'^dashboards/', include('dashboards.foo.urls')),
    url('update-kpis/', update_kpis, name='update-kpis'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
