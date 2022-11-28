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