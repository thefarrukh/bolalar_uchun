from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.common.api_endpoints.serializers import (
    FrontendTranslationSerializer,
    VersionHistorySerializer,
)
from apps.common.models import FrontendTranslation, VersionHistory


class VersionHistoryListCreateView(ListCreateAPIView):
    queryset = VersionHistory.objects.all()
    serializer_class = VersionHistorySerializer


class VersionHistoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = VersionHistory.objects.all()
    serializer_class = VersionHistorySerializer


class FrontendTranslationListCreateView(ListCreateAPIView):
    queryset = FrontendTranslation.objects.all()
    serializer_class = FrontendTranslationSerializer


class FrontendTranslationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = FrontendTranslation.objects.all()
    serializer_class = FrontendTranslationSerializer
