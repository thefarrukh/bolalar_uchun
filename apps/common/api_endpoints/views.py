from rest_framework import viewsets

from apps.common.api_endpoints.serializers import (
    FrontendTranslationSerializer,
    VersionHistorySerializer,
)
from apps.common.models import FrontendTranslation, VersionHistory


class VersionHistoryViewSet(viewsets.ModelViewSet):
    queryset = VersionHistory.objects.all()
    serializer_class = VersionHistorySerializer

class FrontendTranslationViewSet(viewsets.ModelViewSet):
    queryset = FrontendTranslation.objects.all()
    serializer_class = FrontendTranslationSerializer
