from django.conf import settings
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

API_DEFAULT_VERSION = "api/v1"

urlpatterns = [
    path(f'{API_DEFAULT_VERSION}/card/', include("card.urls"), name="card"),
    path(f'{API_DEFAULT_VERSION}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_DEFAULT_VERSION}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="Snippets API",
            default_version='v1',
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns.append(
        path(r'doc/', schema_view.with_ui('swagger', cache_timeout=0), name='api-doc'),
    )
