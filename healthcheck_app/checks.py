"""Health checks for the healthcheck_app."""

import logging

from django.db import connections
from django.db.utils import OperationalError

logger = logging.getLogger(__name__)


def check_database() -> tuple[str, str | None]:
    """Perform the database connectivity check.

    Returns a tuple of the status ('healthy' or 'unhealthy') and an optional error
    message.
    """
    try:
        connections["default"].cursor()  # You could use a specific database alias if needed
    except OperationalError as e:
        logger.debug(f"Health check found an error with the database: {e!s}")
        return "unhealthy", "Error connecting to the database."
    else:
        return "healthy", None
