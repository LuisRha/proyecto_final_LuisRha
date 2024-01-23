from rest_framework.routers import DefaultRouter

from .socio_views import SocioViewSet

router_socio = DefaultRouter()
router_socio.register(prefix='socios', basename='socios',
                      viewset=SocioViewSet)
