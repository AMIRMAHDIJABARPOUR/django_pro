from django.urls import path
from .views import CreateBlogView , post_list , post_info
app_name = "blog"

urlpatterns = [
    path("create/", CreateBlogView.as_view(), name="create"),
    path('post/',post_list,name="post-list"),
    path('post/<int:pk>/',post_info,name='post-info')
    
]