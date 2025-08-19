from django.urls import path

from .views import (
    FrontendTranslationDetailView,
    FrontendTranslationListCreateView,
    VersionHistoryDetailView,
    VersionHistoryListCreateView,
)

urlpatterns = [
    path(
        "version-history/",
        VersionHistoryListCreateView.as_view(),
        name="versionhistory-list",
    ),
    path(
        "version-history/<int:pk>/",
        VersionHistoryDetailView.as_view(),
        name="versionhistory-detail",
    ),
    path(
        "frontend-translation/",
        FrontendTranslationListCreateView.as_view(),
        name="frontendtranslation-list",
    ),
    path(
        "frontend-translation/<int:pk>/",
        FrontendTranslationDetailView.as_view(),
        name="frontendtranslation-detail",
    ),
]
