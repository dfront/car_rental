from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from rent.models import Rent
from client.models import Client, ClientCnhCategory
import logging
logger = logging.getLogger(__name__)

class RentSerializer(serializers.ModelSerializer):
    vehicle_str = serializers.StringRelatedField(many=False)
    class Meta:
        model = Rent
        fields = ('pk','vehicle','vehicle_str','initialDate','endDate','kmRound','client')


    def validate_vehicle(self,data):
        client_id=self.initial_data['client']       
        cnhCategories = ClientCnhCategory.objects.filter(client=Client.objects.get(pk=client_id)).values_list("category__id")
        cnhCategories = list([int(i) for sub in cnhCategories for i in sub])

        if not data.category.cnhCategoryPermited.id in cnhCategories:   
            raise serializers.ValidationError('Categoria de CNH invalida')
        return data


    def create(self,validated_data):
        rent =  Rent.objects.create(**validated_data)
        return rent
