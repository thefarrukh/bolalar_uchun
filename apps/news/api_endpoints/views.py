from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.news.models import Event, Post, Question, QuestionOption, Submission, Survey

from .serializers import (
    EventSerializer,
    PostSerializer,
    QuestionOptionSerializer,
    QuestionSerializer,
    SubmissionSerializer,
    SurveySerializer,
)


# Post
class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Event
class EventListCreateView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Survey
class SurveyListCreateView(ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class SurveyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


# Question
class QuestionListCreateView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# Question Option
class QuestionOptionListCreateView(ListCreateAPIView):
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionSerializer


class QuestionOptionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionSerializer


# Submission
class SubmissionListCreateView(ListCreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class SubmissionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
