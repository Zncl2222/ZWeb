from django.urls import include, path
from rest_framework import routers

from .api.viewsets import SgsimModelViewSet

router = routers.DefaultRouter()
router.register(r'sgsim', SgsimModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
