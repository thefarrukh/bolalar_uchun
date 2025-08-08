# courses/api_endpoints/views.py

from rest_framework import viewsets

from apps.courses.models import Category, Comment, Course, Lesson, Module, Webinar

from .serializers import (
    CategorySerializer,
    CommentSerializer,
    CourseSerializer,
    LessonSerializer,
    ModuleSerializer,
    WebinarSerializer,
)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class WebinarViewSet(viewsets.ModelViewSet):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
