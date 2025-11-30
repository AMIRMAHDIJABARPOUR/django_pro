from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(
        source="author.username",
        read_only=True,
    )

    category_names = serializers.SlugRelatedField(
        source="category",
        many=True,
        read_only=True,
        slug_field="name",
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "author",
            "author_name",
            "category",
            "category_names",
            "content",
            "created_at",
            "updated_at",
        ]
