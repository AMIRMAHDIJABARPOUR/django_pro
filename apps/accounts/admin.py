from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
    ]
    search_fields = ["email", "username", "first_name", "last_name"]
    list_filter = ["is_active", "is_staff", "is_superuser", "date_joined"]
    ordering = ["-date_joined"]
    list_per_page = 10
    list_display_links = ["email", "username"]
    list_editable = ["is_active", "is_staff", "is_superuser"]
