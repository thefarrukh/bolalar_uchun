from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# from django.contrib.auth.forms import AuthenticationForm
from django.urls import include, path

# from django_recaptcha import fields
from .schema import swagger_urlpatterns

# class LoginForm(AuthenticationForm):
#     captcha = fields.ReCaptchaField()

#     def clean(self):
#         captcha = self.cleaned_data.get("captcha")
#         if not captcha:
#             return
#         return super().clean()


# admin.site.login_form = LoginForm
# admin.site.login_template = "login.html"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/common/", include("apps.common.urls", namespace="common")),
    path("api/common/", include("apps.common.api_endpoints.urls")),
    path("api/courses/", include("apps.courses.api_endpoints.urls")),
    path("api/news/", include("apps.news.api_endpoints.urls")),
    path("api/users/", include("apps.users.api_endpoints.urls")),
    path("api/payments/", include("apps.payments.urls", namespace="payments")),
    
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
