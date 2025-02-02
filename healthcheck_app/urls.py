"""URLs for the healthcheck_app."""

from django.conf import settings
from django.urls import path

from .views import health_check

app_name = "healthcheck_app"

url_path = f"{settings.HEALTHCHECK_PATH}/" if settings.HEALTHCHECK_PATH else ""

urlpatterns = [
    path(url_path, health_check, name="healthcheck"),
]
