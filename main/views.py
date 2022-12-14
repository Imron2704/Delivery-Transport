from django.shortcuts import render
from django.views.decorators.cache import cache_page
import time

@cache_page(6 * 10)
def index(request):
    time.sleep(10)
    return render(request, 'index.html')

@cache_page(3 * 10)
def contact(request):
    time.sleep(10)
    return render(request, 'contact.html')

@cache_page(6 * 10)
def blog(request):
    time.sleep(10)
    return render(request, 'blog.html')

@cache_page(6 * 10)
def about_us(request):
    time.sleep(10)
    return render(request, 'aboutus.html')

@cache_page(6 * 10)
def for_business(request):
    time.sleep(10)
    return render(request, 'for-business.html')

@cache_page(5 * 10)
def services(request):
    time.sleep(10)
    return render(request, 'services.html')
    
@cache_page(6 * 10)
def international_shipping(request):
    time.sleep(10)
    return render(request, 'international-shipping.html')

@cache_page(6 * 10)
def individuals(request):
    time.sleep(10)
    return render(request, 'individuals.html')

# from rest_framework import generics, permissions
# from rest_framework.response import Response

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