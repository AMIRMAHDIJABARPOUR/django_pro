from django.contrib import admin
from django.urls import path
from django.urls import include

# from rest_framework.authtoken.views import ObtainAuthToken
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="My Project API",
        default_version="v1",
        description="API documentation for my project.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],  # or IsAuthenticated for private docs
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("apps.accounts.urls")),
    path("api/blog/", include("apps.blog.urls")),
    path("api-auth", include("rest_framework.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path(
        "api-docs/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # ReDoc UI
    path(
        "api-docs/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    # Raw OpenAPI JSON
    path(
        "api-docs/schema.json",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]
