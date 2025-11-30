# from django.shortcuts import get_object_or_404
# from rest_framework.status import (
#     HTTP_200_OK,
#     HTTP_201_CREATED,
#     HTTP_204_NO_CONTENT,
#     HTTP_400_BAD_REQUEST,
# )

from django.db.models import query
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

# local import
from .models import Post
from .serializers import PostSerializer

# Create your views here.


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Post.objects.all()
    serializer_class= PostSerializer

