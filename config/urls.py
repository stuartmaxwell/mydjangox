"""URL configuration for config project."""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

urlpatterns += [
    path(f"{settings.ADMIN_URL}/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("healthcheck/", view=include("healthcheck_app.urls")),
    path("", include("website.urls")),
]
