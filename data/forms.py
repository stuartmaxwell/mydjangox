"""Forms for the model admin."""

from django.contrib.auth import forms

from data import models


class CustomUserCreationForm(forms.AdminUserCreationForm):
    """Custom user creation form for the admin interface."""

    class Meta:
        """Meta class for the custom user creation form."""

        model = models.User

        fields = ("email",)


class CustomUserChangeForm(forms.UserChangeForm):
    """Custom user change form for the admin interface."""

    class Meta:
        """Meta class for the custom user change form."""

        model = models.User

        fields = ("email", "is_active", "is_staff")
