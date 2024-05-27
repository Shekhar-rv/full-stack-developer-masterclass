from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def list_cars(request: HttpRequest):
    return render(request, 'cars/list.html')

def add_car(request: HttpRequest):
    return render(request, 'cars/add.html')

def delete_car(request: HttpRequest):
    return render(request, 'cars/delete.html')