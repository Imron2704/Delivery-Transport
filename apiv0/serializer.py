from main.models import *
from rest_framework import serializers


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_of_Freight
        fields = '__all__'


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculate_the_Cost
        fields = '__all__'


class SubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submit_your_application
        fields = '__all__'