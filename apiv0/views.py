from django.shortcuts import render
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import AboutCompanySerializer
from main.models import About_Company

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class AboutCompanyListAPIView(generics.ListAPIView):
    queryset = About_Company.objects.filter(is_active=True)
    serializer_class = AboutCompanySerializer


class AboutCompanyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = About_Company.objects.all()
    serializer_class = AboutCompanySerializer