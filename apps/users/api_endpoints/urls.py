from django.urls import path

from .auth.views import RegisterView
from .views import (
    InterestDetailView,
    InterestListCreateView,
    UserCourseDetailView,
    UserCourseListCreateView,
    UserDetailView,
    UserListCreateView,
    UserWebinarDetailView,
    UserWebinarListCreateView,
)

urlpatterns = [
    # Users
    path("users/", UserListCreateView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    # Interests
    path("interests/", InterestListCreateView.as_view(), name="interest-list"),
    path("interests/<int:pk>/", InterestDetailView.as_view(), name="interest-detail"),
    # UserCourses
    path("user-courses/", UserCourseListCreateView.as_view(), name="usercourse-list"),
    path(
        "user-courses/<int:pk>/",
        UserCourseDetailView.as_view(),
        name="usercourse-detail",
    ),
    # UserWebinars
    path(
        "user-webinars/", UserWebinarListCreateView.as_view(), name="userwebinar-list"
    ),
    path(
        "user-webinars/<int:pk>/",
        UserWebinarDetailView.as_view(),
        name="userwebinar-detail",
    ),
    path("register/", RegisterView.as_view(), name="user-register"),
]
