from rest_framework.routers import DefaultRouter

from .views import FrontendTranslationViewSet, VersionHistoryViewSet

router = DefaultRouter()
router.register(r'version-histories', VersionHistoryViewSet, basename='versionhistory')
router.register(r'frontend-translations', FrontendTranslationViewSet, basename='frontendtranslation')

urlpatterns = router.urls
