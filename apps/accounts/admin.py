from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "username",
        "password",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
    ]
    fieldsets = (
        ("Login_info", {"fields": ("email", "password")}),
        ("Profile", {"fields": ("username", "first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Date", {"fields": ("last_login",)}),
    )
    search_fields = ["email", "username", "first_name", "last_name"]
    list_filter = ["is_active", "is_staff", "is_superuser", "date_joined"]
    ordering = ["-date_joined"]
    list_per_page = 10
    readonly_fields = ["last_login"]
    list_display_links = ["email", "username"]
    list_editable = ["is_active", "is_staff", "is_superuser"]
