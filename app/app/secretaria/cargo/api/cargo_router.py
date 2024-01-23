from rest_framework.routers import DefaultRouter

from app.secretaria.cargo.api.cargo_views import CargoApiViewSet

router_cargo = DefaultRouter()
router_cargo.register(prefix='cargos', basename='cargos',
                      viewset=CargoApiViewSet)
