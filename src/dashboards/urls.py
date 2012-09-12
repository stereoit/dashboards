from dashboards.api import KPIResource, KPIValueResource, UserResource
from dashboards.api import ColorResource, ColorPaletteResource, DashboardResource
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
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
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}, name="logout"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', \
            {'template_name': 'accounts/login.html' }, name='login'),
    url(r'^$', direct_to_template, {'template':'index.html'}),
    url(r'^dashboards/$', login_required(direct_to_template), {'template':'dashboards.html'}, name="dashboards-index"),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
