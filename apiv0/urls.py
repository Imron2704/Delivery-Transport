from .views import RegisterAPI
from django.urls import path

urlpatterns = [
    path('trucks/', RegisterAPI.as_view(), name='trucks'),
    path('cost/', RegisterAPI.as_view(), name='trucks'),
    path('order/', RegisterAPI.as_view(), name='trucks'),
    path('blog/', RegisterAPI.as_view(), name='trucks'),
    path('calculate/', RegisterAPI.as_view(), name='trucks'),
]