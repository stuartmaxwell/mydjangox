"""The User Profile model."""

from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    """Extends the custom Django User with a Profile model."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # Use the custom user model from settings
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile",
    )
    first_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="User's first name.",
    )
    last_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="User's last name.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options for the User Profile model."""

        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self) -> str:
        """String representation of the UserProfile instance."""
        return str(self.user.email)

    @property
    def full_name(self) -> str:
        """Returns the full name of the user."""
        return f"{self.first_name} {self.last_name}".strip()
