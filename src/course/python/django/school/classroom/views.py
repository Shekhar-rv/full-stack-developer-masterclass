from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    """Home view."""
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    """Thank you view."""
    template_name = 'classroom/thank_you.html'
