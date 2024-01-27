from rest_framework import serializers
from .models import Factory, RetailNetwork, IndividualEntrepreneur, Product


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'


class RetailNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailNetwork
        fields = '__all__'


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
