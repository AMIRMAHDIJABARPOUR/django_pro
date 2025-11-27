from django.contrib import admin
from .models import Post, Category


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "get_categories", "created_at", "updated_at"]
    search_fields = ["title", "author__email", "author__username", "category__name"]
    list_filter = ["created_at", "updated_at", "category"]
    list_per_page = 10
    list_display_links = ["title", "author"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related("category")

    def get_categories(self, obj):
        return ", ".join(c.name for c in obj.category.all())

    get_categories.short_description = "Categories"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
