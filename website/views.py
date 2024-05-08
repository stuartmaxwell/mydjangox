"""Website views file."""

import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """View for the index page."""
    return render(request, "website/index.html")
