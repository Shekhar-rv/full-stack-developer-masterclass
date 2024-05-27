from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('list/', views.list_cars, name='list'),
    path('add/', views.add_car, name='add'),
    path('delete/', views.delete_car, name='delete'),
]