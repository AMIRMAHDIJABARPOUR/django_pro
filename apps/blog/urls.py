from turtle import title
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

# local
from .views import PostModelViewSet, CategoryViewSet


router = DefaultRouter()
router.register("posts", PostModelViewSet, basename="posts")
router.register("categories", CategoryViewSet, basename="category")
app_name = "blog"


urlpatterns = [
    path("", include(router.urls)),
]
