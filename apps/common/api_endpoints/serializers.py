from rest_framework import serializers

from apps.common.models import FrontendTranslation, VersionHistory


class VersionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionHistory
        fields = '__all__'

class FrontendTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontendTranslation
        fields = '__all__'
        ref_name = "FrontendTranslationSerializerFromApiEndpoints"  
