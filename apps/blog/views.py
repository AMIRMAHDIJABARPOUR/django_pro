from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# local import
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from . import permissions
from .filter import PostFilter

# Create your views here.


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_fields = ["title", "content"]
    Ordering_fields = ["created_at", "updated_at", "title"]


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
