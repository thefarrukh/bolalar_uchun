# apps/users/api_endpoints/views.py

from rest_framework import viewsets

from apps.users.models import Interest, User, UserCourse, UserWebinar

from .serializers import (
    InterestSerializer,
    UserCourseSerializer,
    UserSerializer,
    UserWebinarSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer


class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


class UserCourseViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


class UserWebinarViewSet(viewsets.ModelViewSet):
    queryset = UserWebinar.objects.all()
    serializer_class = UserWebinarSerializer
