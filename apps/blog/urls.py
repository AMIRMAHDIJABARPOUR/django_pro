from turtle import title
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

# local
from .views import PostModelViewSet, CategoryViewSet

from django.contrib import admin
from django.urls import path, include
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


router = DefaultRouter()
router.register("posts", PostModelViewSet, basename="posts")
router.register("categories", CategoryViewSet, basename="category")
app_name = "blog"


urlpatterns = [
    path("", include(router.urls)),
]
