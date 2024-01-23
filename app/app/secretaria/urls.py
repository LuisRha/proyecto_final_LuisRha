from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .cargo.api.cargo_router import router_cargo
from .socio.api.socio_router import router_socio

router = DefaultRouter()

urlpatterns = [
    path('', include(router_cargo.urls)),
    path('', include(router_socio.urls)),
]
