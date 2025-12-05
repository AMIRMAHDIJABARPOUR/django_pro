from django.urls import path, include
from rest_framework.routers import DefaultRouter

# local import
from .views import UserViewSet, ProfileViewSet

app_name = "accounts"
router = DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("profiles", ProfileViewSet, basename="profile")
urlpatterns = [
    path("", include(router.urls)),
]
