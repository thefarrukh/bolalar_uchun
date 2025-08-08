# apps/news/api_endpoints/urls.py

from rest_framework.routers import DefaultRouter

from .views import (
    EventViewSet,
    PostViewSet,
    QuestionOptionViewSet,
    QuestionViewSet,
    SubmissionViewSet,
    SurveyViewSet,
)

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"events", EventViewSet)
router.register(r"surveys", SurveyViewSet)
router.register(r"questions", QuestionViewSet)
router.register(r"question-options", QuestionOptionViewSet)
router.register(r"submissions", SubmissionViewSet)

urlpatterns = router.urls
