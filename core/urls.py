from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    # Common app
    path("api/v1/common/", include("apps.common.urls", namespace="common")),
    # path("api/common/", include("apps.common.api_endpoints.urls")),  # endi router emas, path list boladi
    # Courses app
    # path("api/courses/", include("apps.courses.api_endpoints.urls")),
    # News app
    # path("api/news/", include("apps.news.api_endpoints.urls")),
    # Users app
    # path("api/users/", include("apps.users.api_endpoints.urls")),
    # Payments app
    path("api/payments/", include("apps.payments.urls", namespace="payments")),
    # JWT Auth
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
