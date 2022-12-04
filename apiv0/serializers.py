from main.models import *
from rest_framework import serializers


## Class Truck Serializers


# class TruckSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Truck
#         fields = '__all__'


##########

class TruckCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryForTruck
        fields = ('id', 'title')


class TruckImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck_Images
        fields = ('id', 'get_image_url')


class TruckSerializer(serializers.ModelSerializer):
    truck_images = TruckImagesSerializer(many=True)

    class Meta:
        model = Truck
        fields = ('__all__')


## Class Cost Serializers



class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculate_The_Cost
        fields = '__all__'


## Class Cost Delivery Serializers


class CostDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost_Of_Delivery
        fields = '__all__'


## Unloading and Loading Serializers


class UnloadingAndLoadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unloading_And_Loading
        fields = '__all__'


## Class Delivery Method Serializers



class DeliveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_Method
        fields = '__all__'


## Class Submit The Application Serializers


class SubmitTheApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submit_Your_Application
        fields = '__all__'


## Class Our Services Serializers


class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_Services
        fields = '__all__'


## Class About Company Serializers


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


## Class Contact Serializers



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'title',
            'phone_number',
            'status',
            'description',
            'from_here',
            'to_here'
        )


## Class Blog Serializer



class CategoryBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Blog
        fields = ('id', 'title')


class BlogImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_Images
        fields = ('id', 'get_image_url')


class BlogSerializer(serializers.ModelSerializer):
    blog_images = BlogImagesSerializer(many=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'category', 'description', 'blog_images')


## Class Order Serializers


class WeightCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightCargo
        fields = '__all__'


class VolumeCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LengthCargo
        fields = '__all__'


class TypeCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCargo
        fields = '__all__'


class ModeCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeCargo
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'id',
            'title',
            'user',
            'from_here',
            'to_here',
            'phone_number',
            'weight_cargo',
            'volume_cargo',
            'type_cargo',
            'mode_cargo',
            'date_created',
            'car',
            'image_1',
            'image_2',
            'image_3',
        )


class OrderGETSerializer(serializers.ModelSerializer):
    car = TruckSerializer()
    weight_cargo = WeightCargoSerializer()
    volume_cargo = VolumeCargoSerializer()
    type_cargo = TypeCargoSerializer()
    mode_cargo = ModeCargoSerializer()

    class Meta:
        model = Order
        fields = (
            'transaction_id',
            'title',
            'from_here',
            'to_here',
            'phone_number',
            'weight_cargo',
            'volume_cargo',
            'type_cargo',
            'mode_cargo',
            'date_created',
            'car',
            'image_1',
            'image_2',
            'image_3',
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'transaction_id',
            'user',
            'car',
            'title',
            'date_created',
            'from_here',
            'to_here',
            'phone_number',
            'weight_cargo',
            'volume_cargo',
            'type_cargo',
            'mode_cargo',
            'image_1',
            'image_2',
            'image_3',
        )


## Class Work Principles Serializer


class WorkPrinciplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_Principles
        fields = ('__all__')
