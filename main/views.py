from django.shortcuts import render
from django.views.decorators.cache import cache_page
import time

@cache_page(6 * 10)
def index(request):
    time.sleep(10)
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blog_post(request):
    return render(request, 'blog-post.html')

def index13(request):
    return render(request, 'index13.html')

def photos(request):
    return render(request, 'photos.html')

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