from rest_framework import serializers
from vehicle.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    model = serializers.StringRelatedField(many=False)
    class Meta:
        model = Vehicle
        fields = ('pk','category','model','km','board')
