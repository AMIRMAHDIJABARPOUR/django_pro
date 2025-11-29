from django.shortcuts import get_object_or_404
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer

# Create your views here.


class post_list(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        post = Post.objects.all()
        serializer = self.serializer_class(post, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class post_info(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)


