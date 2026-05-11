"""Website views file."""

import logging
from typing import TYPE_CHECKING

from django.shortcuts import render

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """View for the index page."""
    return render(request, "website/index.html")
