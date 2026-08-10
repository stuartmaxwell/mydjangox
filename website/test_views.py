"""Tests for the website app."""

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_index_view(client):
    """Test the index view."""
    url = reverse("website:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome" in response.content
    assertTemplateUsed(response, "website/index.html")
