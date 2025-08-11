from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.courses.models import Category, Comment, Course, Lesson, Module, Webinar
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    CourseSerializer,
    LessonSerializer,
    ModuleSerializer,
    WebinarSerializer,
)

# Course
class CourseListCreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Webinar
class WebinarListCreateView(ListCreateAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer

class WebinarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer


# Category
class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Module
class ModuleListCreateView(ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


# Lesson
class LessonListCreateView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


# Comment
class CommentListCreateView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
