from django.conf.urls import url
from rest_framework import routers
from servicio.restapi.views import PersonaViewSet, TareaViewSet, ReporteViewSet


router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet, base_name='persona')
router.register(r'tarea', TareaViewSet)
router.register(r'reporte', ReporteViewSet)


urlpatterns = router.urls