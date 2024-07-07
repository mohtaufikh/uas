from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SantriViewSet

router = DefaultRouter()
router.register('santri', SantriViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
