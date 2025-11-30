from django.urls import path , include

from rest_framework.routers import DefaultRouter

from .views import PostModelViewSet


router=DefaultRouter()
router.register('posts',PostModelViewSet,basename='posts')
app_name = "blog"


urlpatterns = [
    path('', include(router.urls))
]
