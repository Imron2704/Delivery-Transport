from django.shortcuts import render
from django.views.decorators.cache import cache_page
import time

@cache_page(6 * 10)
def index(request):
    time.sleep(10)
    return render(request, 'index.html')

@cache_page(6 * 10)
def contact(request):
    time.sleep(10)
    return render(request, 'contact.html')

@cache_page(6 * 10)
def blog(request):
    time.sleep(10)
    return render(request, 'blog.html')

@cache_page(6 * 10)
def blog_post(request):
    time.sleep(10)
    return render(request, 'aboutus.html')

@cache_page(6 * 10)
def index13(request):
    time.sleep(10)
    return render(request, 'forbusiness.html')

@cache_page(6 * 10)
def photos(request):
    time.sleep(10)
    return render(request, 'services.html')
    
@cache_page(6 * 10)
def photos(request):
    time.sleep(10)
    return render(request, 'international shipping.html')

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