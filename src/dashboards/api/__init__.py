from tastypie.api import Api
from dashboards.api.resources import UserResource, KPIResource, KPIValueResource, \
ColorPaletteResource, ColorResource, DashboardResource, KPIGeneratorResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(KPIValueResource())
v1_api.register(KPIResource())
v1_api.register(ColorResource())
v1_api.register(ColorPaletteResource())
v1_api.register(DashboardResource())
v1_api.register(KPIGeneratorResource())

