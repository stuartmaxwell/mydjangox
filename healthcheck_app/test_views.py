import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_health_check_view_response_format(client):
    url = reverse("healthcheck_app:healthcheck")
    response = client.get(url)
    # Verify response is JSON
    assert response.headers["Content-Type"] == "application/json"
    # Verify response contains status field with healthy value
    response_data = response.json()
    assert "status" in response_data
    assert response_data["status"] == "healthy"
