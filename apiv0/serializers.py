from main.models import *
from rest_framework import serializers


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculate_The_Cost
        fields = '__all__'


class SubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submit_Your_Application
        fields = '__all__'


