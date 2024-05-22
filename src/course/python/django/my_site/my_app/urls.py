from django.urls import path
from . import views

urlpatterns = [
    path('', views.example_view, name='example_view'),
    path('variable/', views.variable_view, name='variable_view'),
]