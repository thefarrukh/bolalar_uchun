# courses/api_endpoints/urls.py

from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    CommentViewSet,
    CourseViewSet,
    LessonViewSet,
    ModuleViewSet,
    WebinarViewSet,
)

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")
router.register(r"webinars", WebinarViewSet, basename="webinar")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"modules", ModuleViewSet, basename="module")
router.register(r"lessons", LessonViewSet, basename="lesson")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = router.urls
