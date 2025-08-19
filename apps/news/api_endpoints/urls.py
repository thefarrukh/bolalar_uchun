from django.urls import path

from .views import (
    EventDetailView,
    EventListCreateView,
    PostDetailView,
    PostListCreateView,
    QuestionDetailView,
    QuestionListCreateView,
    QuestionOptionDetailView,
    QuestionOptionListCreateView,
    SubmissionDetailView,
    SubmissionListCreateView,
    SurveyDetailView,
    SurveyListCreateView,
)

urlpatterns = [
    # Posts
    path("posts/", PostListCreateView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    # Events
    path("events/", EventListCreateView.as_view(), name="event-list"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="event-detail"),
    # Surveys
    path("surveys/", SurveyListCreateView.as_view(), name="survey-list"),
    path("surveys/<int:pk>/", SurveyDetailView.as_view(), name="survey-detail"),
    # Questions
    path("questions/", QuestionListCreateView.as_view(), name="question-list"),
    path("questions/<int:pk>/", QuestionDetailView.as_view(), name="question-detail"),
    # Question Options
    path(
        "question-options/",
        QuestionOptionListCreateView.as_view(),
        name="questionoption-list",
    ),
    path(
        "question-options/<int:pk>/",
        QuestionOptionDetailView.as_view(),
        name="questionoption-detail",
    ),
    # Submissions
    path("submissions/", SubmissionListCreateView.as_view(), name="submission-list"),
    path(
        "submissions/<int:pk>/",
        SubmissionDetailView.as_view(),
        name="submission-detail",
    ),
]
