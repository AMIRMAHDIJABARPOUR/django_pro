from rest_framework import serializers
from .models import User, Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="accounts:profile-detail"
    )

    class Meta:
        model = User
        fields = ["id", "username", "email", "profile", "profile"]
        extra_kwargs = {
            "url": {"view_name": "accounts:user-detail", "lookup_field": "pk"},
        }


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user_username = serializers.CharField(
        source="user.username",
        read_only=True,
    )

    class Meta:
        model = Profile
        fields = ["id", "user", "user_username", "bio", "location", "birth_date", "url"]
        extra_kwargs = {
            "url": {"view_name": "accounts:profile-detail", "lookup_field": "pk"},
            "user": {"view_name": "accounts:user-detail", "lookup_field": "pk"},
        }
