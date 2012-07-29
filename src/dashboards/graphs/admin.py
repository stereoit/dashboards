from django.contrib import admin
from dashboards.graphs.models import KPI, KPIValue, ColorPalette
from dashboards.graphs.models import Color, Graph

admin.site.register(KPI)
admin.site.register(KPIValue)
admin.site.register(ColorPalette)
admin.site.register(Color)
admin.site.register(Graph)
