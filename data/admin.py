"""Admin configuration for models."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from data import forms, models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom user admin class for the User model."""

    add_form = forms.CustomUserCreationForm

    form = forms.CustomUserChangeForm
    model = models.User

    ordering = ("email",)
    list_display = ("email", "is_active", "is_email_verified", "is_staff", "is_superuser")
    search_fields = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_email_verified", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2", "is_staff")}),)


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Custom admin class for the UserProfile model."""

    list_display = [
        "user",
        "first_name",
        "last_name",
        "created_at",
        "updated_at",
    ]

    search_fields = ["user__email", "first_name", "last_name"]

    ordering = ["user__email"]

    list_filter = ["user__is_active"]
