from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["url", "id", "name"]
        extra_kwargs = {
            "url": {"view_name": "blog:category-detail", "lookup_field": "pk"}
        }


class PostSerializer(serializers.HyperlinkedModelSerializer):
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
    snippet = serializers.ReadOnlyField(source="get_snippet")

    class Meta:
        model = Post
        fields = [
            "url",
            "id",
            "title",
            "author",
            "author_name",
            "category",
            "category_names",
            "content",
            "created_at",
            "updated_at",
            "snippet",
        ]
        extra_kwargs = {
            "url": {"view_name": "blog:posts-detail", "lookup_field": "pk"},
            "author": {"view_name": "accounts:user-detail", "lookup_field": "pk"},
            "category": {"view_name": "blog:category-detail", "lookup_field": "pk"},
        }

    def get_snippet(self, obj):
        return obj.content[:20] + "..."  # Return the first 100 characters as a snippet

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        view = self.context.get("view")
        action = getattr(
            view, "action", None
        )  # , "created_at", "updated_at", "category"
        if action == "list":
            representation.pop("content", None)
            representation.pop("created_at", None)
            representation.pop("updated_at", None)
            representation.pop("category", None)
        elif action == "retrieve":
            representation.pop("snippet", None)
            representation.pop("absolute_api_url", None)
        return representation
