from rest_framework import viewsets
from .models import Factory, RetailNetwork, IndividualEntrepreneur, Product
from .permissions import IsOwnerOrStaff
from .serializers import FactorySerializer, RetailNetworkSerializer, IndividualEntrepreneurSerializer, ProductSerializer
from rest_framework import filters, permissions

# Create your views here.


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]


class RetailNetworkViewSet(viewsets.ModelViewSet):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']


class IndividualEntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]

    def partial_update(self, request, *args, **kwargs):
        # Запрещаем обновление поля 'debt_to_supplier'
        if 'debt_to_supplier' in request.data:
            del request.data['debt_to_supplier']
        return super().partial_update(request, *args, **kwargs)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]
