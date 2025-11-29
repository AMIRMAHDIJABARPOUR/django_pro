from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("apps.accounts.urls")),
    path("api/blog/", include("apps.blog.urls")),
    path("api-auth", include("rest_framework.urls")),
]
