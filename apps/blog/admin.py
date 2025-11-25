from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at", "updated_at"]
    search_fields = ["title", "author__email", "author__username"]
    list_filter = ["created_at", "updated_at"]
    list_per_page = 10
    list_display_links = ["title", "author"]
