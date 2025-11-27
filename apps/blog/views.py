from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
class CreateBlogView(APIView):
    pass

@api_view(['GET'])
def post_list(request):
    return Response({"message": "Hello, World!"})