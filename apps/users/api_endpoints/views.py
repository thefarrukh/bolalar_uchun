from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.users.models import Interest, User, UserCourse, UserWebinar

from .serializers import (
    InterestSerializer,
    UserCourseSerializer,
    UserSerializer,
    UserWebinarSerializer,
)


# User
class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer


# Interest
class InterestListCreateView(ListCreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


class InterestDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


# UserCourse
class UserCourseListCreateView(ListCreateAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


class UserCourseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


# UserWebinar
class UserWebinarListCreateView(ListCreateAPIView):
    queryset = UserWebinar.objects.all()
    serializer_class = UserWebinarSerializer


class UserWebinarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserWebinar.objects.all()
    serializer_class = UserWebinarSerializer
