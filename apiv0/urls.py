# from .views import RegisterAPI
from django.urls import path, include
from django.urls import path
from .views import *


urlpatterns = [
    # path('trucks/', RegisterAPI.as_view(), name='trucks'),
    # path('cost/', RegisterAPI.as_view(), name='trucks'),
    # path('order/', RegisterAPI.as_view(), name='trucks'),
    # path('blog/', RegisterAPI.as_view(), name='trucks'),
    # path('calculate/', RegisterAPI.as_view(), name='trucks'),
    # path('about/', include('apiv0.urls')),

    ## About Company Urls

    path('about-company/', AboutCompanyListAPIView.as_view()),
    path('about-company/<int:pk>/', AboutCompanyRetrieveAPIView.as_view()),
    
    ## Contact Urls

    path('create/', ContactCreateAPIView.as_view()),
    path('list/', ContactListAPIView.as_view()),

    ## Truck Urls


    path('category/', CategoryTruckListAPIView.as_view()),
    path('category/<int:pk>/', CategoryTruckRetrieveAPIView.as_view()),
    path('auto-cars/', TruckListAPIView.as_view()),
    path('auto-car/<int:pk>/', TruckRetrieveAPIView.as_view()),

    ## Blog Urls

    path('category/', CategoryBlogListAPIView.as_view()),
    path('category/<int:pk>/', CategoryBlogRetrieveAPIView.as_view()),
    path('articles/', BlogListAPIView.as_view()),
    path('article/<int:pk>/', BlogRetrieveAPIView.as_view()),

    ## Order Urls

    path('Order-api-view/', OrderListAPIView.as_view()),
    path('Order-api-view/create', OrderCreateAPIView.as_view()),
    path('retrieve/<str:transaction_id>/', OrderRetrieveAPIView.as_view()),


    ## Work Principles Urls

    path('create/', WokrPrinciplesCreateAPIView.as_view()),
    path('list/', WorkPrinciplestListAPIView.as_view()),


    ## Cost Delivery Urls

    path('create/', CostDeliveryCreateAPIView.as_view()),
    path('list/', CostDeliverytListAPIView.as_view()),

    ## Our Services Urls

    path('create/', OurServicesCreateAPIView.as_view()),
    path('list/', OurServicesListAPIView.as_view()),

    ## Our Delivery Method Urls

    path('create/', DeliveryMethodDeliveryCreateAPIView.as_view()),
    path('list/', DeliveryMethodDeliverytListAPIView.as_view()),

    ## Our Submit Yout Application Urls

    path('create/', SubmitApplicationCreateAPIView.as_view()),
    path('list/', SubmitApplicationListAPIView.as_view()),

    ## Unloading and Loading Urls

    path('create/', UnloadingAndLoadingCreateAPIView.as_view()),
    path('list/', UnloadingAndLoadingListAPIView.as_view()),


    ##### Trucks/apiv0 #####
    # path('teachers/', TeacherViewSet.as_view({'get': 'list'}), name = 'teachers'),
    # path('teachers/create', TeacherCreateView.as_view()),
    # path('teachers/change', TeacherUpdateView.as_view()),
    # path('teachers/delete', TeacherDestroyView.as_view()),
    # ##### Students/apiv0 #####
    # path('students/', StudentViewSet.as_view({'get': 'list'}), name = 'students'),
    # path('students/create', StudentCreateView.as_view()),
    # path('students/change', StudentUpdateView.as_view()),
    # path('students/delete', StudentDestroyView.as_view()),
    # ##### Subjects/apiv0 #####
    # path('subjects/', SubjectViewSet.as_view({'get': 'list'}), name = 'subjects'),
    # path('subjects/create', SubjectCreateView.as_view()),
    # path('subjects/change', SubjectUpdateView.as_view()),
    # path('subjects/delete', SubjectDestroyView.as_view()),
    
    # ##### Api Token SimpleJWT #####
    # path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name = 'token_verify'),
]