from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResultModelViewSet


router = DefaultRouter()
router.register(r'results', ResultModelViewSet, basename='results')

urlpatterns = [
    path('zimsec/', include(router.urls))
]