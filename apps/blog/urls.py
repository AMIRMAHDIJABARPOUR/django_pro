from django.urls import path
from .views import post_list, post_info

app_name = "blog"

urlpatterns = [
    # path("create/", CreateBlogView.as_view(), name="create"),
    path("post/", post_list.as_view(), name="post-list"),
    path("post/<int:pk>/", post_info.as_view(), name="post-info"),
]
