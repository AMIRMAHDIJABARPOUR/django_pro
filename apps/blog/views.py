from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# local import
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer

# Create your views here.


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
