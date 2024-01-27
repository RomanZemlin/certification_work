from rest_framework import viewsets
from .models import Factory, RetailNetwork, IndividualEntrepreneur, Product
from .serializers import FactorySerializer, RetailNetworkSerializer, IndividualEntrepreneurSerializer, ProductSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [IsAuthenticated]


class RetailNetworkViewSet(viewsets.ModelViewSet):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']


class IndividualEntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Запрещаем обновление поля 'debt_to_supplier'
        if 'debt_to_supplier' in request.data:
            del request.data['debt_to_supplier']
        return super().update(request, *args, **kwargs)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
