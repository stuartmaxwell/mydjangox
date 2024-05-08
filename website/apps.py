"""Apps configuration for website app."""

from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    """Website app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "website"
