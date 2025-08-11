from django.urls import path
from .views import (
    CourseListCreateView, CourseDetailView,
    WebinarListCreateView, WebinarDetailView,
    CategoryListCreateView, CategoryDetailView,
    ModuleListCreateView, ModuleDetailView,
    LessonListCreateView, LessonDetailView,
    CommentListCreateView, CommentDetailView,
)

urlpatterns = [
    # Courses
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    # Webinars
    path('webinars/', WebinarListCreateView.as_view(), name='webinar-list'),
    path('webinars/<int:pk>/', WebinarDetailView.as_view(), name='webinar-detail'),

    # Categories
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Modules
    path('modules/', ModuleListCreateView.as_view(), name='module-list'),
    path('modules/<int:pk>/', ModuleDetailView.as_view(), name='module-detail'),

    # Lessons
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),

    # Comments
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
