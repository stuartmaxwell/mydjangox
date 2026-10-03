"""Website views file."""

import logging
from typing import TYPE_CHECKING

from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import View

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


logger = logging.getLogger(__name__)


class HomeView(View):
    """View for the home page."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Render the landing page."""
        return TemplateResponse(request, "website/home.html")
