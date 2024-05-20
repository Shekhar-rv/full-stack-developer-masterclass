from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') # first_app/urls.py
]
