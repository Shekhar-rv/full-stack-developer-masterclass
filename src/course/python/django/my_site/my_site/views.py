from django.shortcuts import render
from django.http import HttpRequest


def my_custom_page_not_found_view(request: HttpRequest, exception): # type: ignore
    """
    View for custom 404 page
    """
    return render(request, '404.html', {'exception': exception}, status=404)
