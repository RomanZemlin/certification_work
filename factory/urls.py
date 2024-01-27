from django.urls import include, path
from rest_framework import routers
from factory.views import FactoryViewSet, RetailNetworkViewSet, IndividualEntrepreneurViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'factories', FactoryViewSet)
router.register(r'retail_networks', RetailNetworkViewSet)
router.register(r'individual_entrepreneurs', IndividualEntrepreneurViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
