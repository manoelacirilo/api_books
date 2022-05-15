from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ("id", "name", "email", "created_at", "updated_at")
    list_filter = ("is_active", "is_staff", "groups")
    search_fields = ("email",)
    ordering = ("email", "name")
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)


admin.site.register(User, CustomUserAdmin)
