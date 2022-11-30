from main.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
