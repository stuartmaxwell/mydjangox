"""App configuration for the data app."""

from django.apps import AppConfig


class DataConfig(AppConfig):
    """Data app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "data"
