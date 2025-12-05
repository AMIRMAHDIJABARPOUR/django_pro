from rest_framework import viewsets
from rest_framework.permissions import AllowAny as All

# local import
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [All]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [All]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
