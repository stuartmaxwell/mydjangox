"""Website URLs file."""

from django.urls import path

from interfaces.website import views

app_name = "website"

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
]
