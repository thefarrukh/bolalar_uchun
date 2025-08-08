# apps/users/api_endpoints/urls.py

from rest_framework.routers import DefaultRouter

from .views import (
    InterestViewSet,
    UserCourseViewSet,
    UserViewSet,
    UserWebinarViewSet,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"interests", InterestViewSet)
router.register(r"user-courses", UserCourseViewSet)
router.register(r"user-webinars", UserWebinarViewSet)

urlpatterns = router.urls
