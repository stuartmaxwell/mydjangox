"""App configuration for healthcheck_app."""

from django.apps import AppConfig


class HealthcheckAppConfig(AppConfig):
    """App configuration for the healthcheck app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "healthcheck_app"
