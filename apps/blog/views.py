from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
# Create your views here.
class CreateBlogView(APIView):
    pass

@api_view(['GET','POST'])
def post_list(request):
    if request.method=="GET":
        posts=Post.objects.all()
        serializer=PostSerializer(posts, many=True)
        return Response(serializer.data,status=HTTP_200_OK)
    if request.method=="POST":
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            post=serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.error,status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def post_info(request,pk):
    if request.method=="GET":
        posts=get_object_or_404(Post,pk=pk)
        serializer=PostSerializer(posts)
        return Response(serializer.data,status=HTTP_200_OK)
    elif request.method=="PUT":
        post=get_object_or_404(Post,pk=pk)
        serialize=PostSerializer(post,request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=HTTP_200_OK)
        return Response(serialize.error_messages,status=HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        post=get_object_or_404(Post,pk=pk)
        post.delete()
        return Response({"detail": f"Post '{post.title}' has been deleted successfully."},status=HTTP_204_NO_CONTENT)