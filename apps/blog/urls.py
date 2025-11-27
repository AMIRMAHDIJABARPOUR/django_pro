from django.urls import path
from .views import CreateBlogView , post_list
app_name = "blog"

urlpatterns = [
    path("create/", CreateBlogView.as_view(), name="create"),
    path('',post_list,name="post-list"),
]