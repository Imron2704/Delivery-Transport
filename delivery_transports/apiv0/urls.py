from .views import RegisterAPI
from django.urls import path

urlpatterns = [
    path('trucks/', RegisterAPI.as_view(), name='trucks'),
    path('cost/', RegisterAPI.as_view(), name='trucks'),
    path('order/', RegisterAPI.as_view(), name='trucks'),
    path('blog/', RegisterAPI.as_view(), name='trucks'),
    path('calculate/', RegisterAPI.as_view(), name='trucks'),

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