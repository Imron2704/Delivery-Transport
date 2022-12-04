from django.shortcuts import render
# from .serializers import UserSerializer, RegisterSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import AboutCompanySerializer
from main.models import About_Company
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from main.models import Order
from .serializers import OrderSerializer, OrderCreateSerializer

# from accounts.permissions import IsOwnUserOrReadOnly, IsAuthenticated


# Register API
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#         "token": AuthToken.objects.create(user)[1]
#         })


## Class About Company ApiView


class AboutCompanyListAPIView(generics.ListAPIView):
    queryset = About_Company.objects.filter(is_active=True)
    serializer_class = AboutCompanySerializer


class AboutCompanyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = About_Company.objects.all()
    serializer_class = AboutCompanySerializer


## Class Contact ApiView


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


## Class Truck ApiView


class CategoryTruckListAPIView(generics.ListAPIView):
    queryset = CategoryForTruck.objects.filter(is_active=True)
    serializer_class = TruckCategorySerializer


class CategoryTruckRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CategoryForTruck.objects.all()
    serializer_class = TruckCategorySerializer


class TruckListAPIView(generics.ListAPIView):
    queryset = Truck.objects.filter(is_active=True)
    serializer_class = TruckSerializer


class TruckRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


## Blog ApiView


class CategoryBlogListAPIView(generics.ListAPIView):
    queryset = Category_Blog.objects.filter(is_active=True)
    serializer_class = CategoryBlogSerializer


class CategoryBlogRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category_Blog.objects.all()
    serializer_class = CategoryBlogSerializer


class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializer


class BlogRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


## Class Order ApiView


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (IsOwnUserOrReadOnly)


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    # permission_classes = (IsOwnUserOrReadOnly)


class OrderRetrieveAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated)
    lookup_field = 'id'



## Class Wokr Principles ApiView


class WokrPrinciplesCreateAPIView(generics.CreateAPIView):
    queryset = Work_Principles.objects.all()
    serializer_class = WorkPrinciplesSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class WorkPrinciplestListAPIView(generics.ListAPIView):
    queryset = Work_Principles.objects.all()
    serializer_class = WorkPrinciplesSerializer


## Class Cost Of Delivery ApiView


class CostDeliveryCreateAPIView(generics.CreateAPIView):
    queryset = Cost_Of_Delivery.objects.all()
    serializer_class = WorkPrinciplesSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CostDeliverytListAPIView(generics.ListAPIView):
    queryset = Cost_Of_Delivery.objects.all()
    serializer_class = WorkPrinciplesSerializer


## Class Delivery Method ApiView


class DeliveryMethodDeliveryCreateAPIView(generics.CreateAPIView):
    queryset = Delivery_Method.objects.all()
    serializer_class = DeliveryMethodSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DeliveryMethodDeliverytListAPIView(generics.ListAPIView):
    queryset = Delivery_Method.objects.all()
    serializer_class = DeliveryMethodSerializer


## Class Unloading and Loading ApiView


class UnloadingAndLoadingCreateAPIView(generics.CreateAPIView):
    queryset = Unloading_And_Loading.objects.all()
    serializer_class = UnloadingAndLoadingSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UnloadingAndLoadingListAPIView(generics.ListAPIView):
    queryset = Unloading_And_Loading.objects.all()
    serializer_class = UnloadingAndLoadingSerializer


## Class Submit Your Application ApiView


class SubmitApplicationCreateAPIView(generics.CreateAPIView):
    queryset = Submit_Your_Application.objects.all()
    serializer_class = SubmitTheApplicationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SubmitApplicationListAPIView(generics.ListAPIView):
    queryset = Submit_Your_Application.objects.all()
    serializer_class = SubmitTheApplicationSerializer


## Class Our Services ApiView


class OurServicesCreateAPIView(generics.CreateAPIView):
    queryset = Our_Services.objects.all()
    serializer_class = OurServicesSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OurServicesListAPIView(generics.ListAPIView):
    queryset = Our_Services.objects.all()
    serializer_class = OurServicesSerializer
