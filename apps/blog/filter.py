import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    author__username = django_filters.CharFilter(
        field_name="author__username", lookup_expr="icontains"
    )
    category__name = django_filters.CharFilter(
        field_name="category__name", lookup_expr="icontains"
    )
    create_before = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte"
    )
    create_after = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "author",
            "category",
            "created_at",
        ]
