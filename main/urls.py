from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('contact/', contact, name = 'contact'),
    path('blog/', blog, name = 'blog'),
    path('about-us/', about_us, name = 'aboutus'),
    path('for-business/', for_business, name = 'for-business'),
    path('services/', services, name = 'services'),
    path('international-shipping/', international_shipping, name = 'international-shipping'),
    path('individuals/', individuals, name = 'individuals'),
]