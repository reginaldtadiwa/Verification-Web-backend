
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KycModelViewSet


router = DefaultRouter()
router.register(r'customerkyc', KycModelViewSet, basename='customer_kyc')

urlpatterns = [
    path('crz/', include(router.urls))
]