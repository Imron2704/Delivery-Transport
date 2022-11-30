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


class AboutCompanyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Company_Images
        fields = (
            'id', 'image'
        )


class AboutCompanySerializer(serializers.ModelSerializer):
    about_images = AboutCompanyImagesSerializer(many=True)

    class Meta:
        model = About_Company
        fields = (
            'id',
            'title',
            'description',
            'about_images',
        )



