"""Views for the healthcheck_app."""

import logging

from django.http import HttpRequest, JsonResponse
from django.utils import timezone

from healthcheck_app.checks import check_database

logger = logging.getLogger(__name__)

# Checks to perform, with their corresponding check functions
checks = {
    "database": check_database,
}


def health_check(_: HttpRequest) -> JsonResponse:
    """Main function that returns the healthcheck.

    Perform a health check on the application by checking various components.
    Returns a JsonResponse with the health information of the components.
    """
    # Initial health data structure
    health_data = {
        "status": "healthy",  # Starts assuming everything is healthy
        "timestamp": timezone.now().isoformat(),
        "details": {},
    }

    # Iterate over the checks and perform them
    for check_name, check_function in checks.items():
        status, error = check_function()

        # Update the component's status in the health data
        health_data["details"][check_name] = {"status": status}

        # If there's an error, add it to the component's data
        if error:
            health_data["details"][check_name]["error"] = error

        # If any component is unhealthy, set overall status to 'unhealthy'
        if status == "unhealthy":
            health_data["status"] = "unhealthy"

    # Return the JsonResponse with the health data and status code
    return JsonResponse(health_data)
