from django.shortcuts import render
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

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


# class TeacherViewSet(viewsets.ModelViewSet):
#     serializer_class = TeacherSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         q = Teacher.objects.all()
#         url_dict = self.request.GET
#         print(url_dict)
#         if 'search-text' in url_dict and url_dict['search-text']:
#             text = url_dict.get('search-text')
#             q = q.filter(Q(name__icontains=text))
#         return q


# class TeacherCreateView(generics.CreateAPIView):
#     serializer_class = TeacherSerializer


# class TeacherUpdateView(generics.UpdateAPIView):
#     serializer_class = TeacherSerializer

#     def get_object(self):
#         return Teacher.objects.get(pk = self.request.data.get('id'))


# class TeacherDestroyView(generics.DestroyAPIView):
#     serializer_class = TeacherSerializer

#     def get_object(self):
#         return Teacher.objects.get(pk = self.request.data.get('id'))