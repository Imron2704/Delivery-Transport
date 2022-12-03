from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('delivery_transports.main.urls')),
    path('v0/', include('delivery_transports.apiv0.urls')),
    path('accounts/', include('delivery_transports.accounts.urls')),
]

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
