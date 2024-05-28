from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
from . import models

# Create your views here.

def list_cars(request: HttpRequest):
    """
    List all cars in the database.
    """
    all_cars = models.Car.objects.all()
    return render(request, 'cars/list.html', context={'all_cars': all_cars})

def add_car(request: HttpRequest):
    """
    Add a new car to the database.
    """
    if not request.POST:
        return render(request, 'cars/add.html')
    brand = request.POST.get('brand')
    year = int(request.POST.get('year')) # type: ignore
    models.Car.objects.create(brand=brand, year=year)
    # If user submits the form, redirect to the list page
    return redirect(reverse('cars:list'))

def delete_car(request: HttpRequest):
    """
    Delete a car from the database.
    """
    if not request.POST:
        return render(request, 'cars/delete.html')
    pk = int(request.POST.get('pk')) # type: ignore
    try:
        models.Car.objects.get(pk=pk).delete()
        return redirect(reverse('cars:list'))
    except models.Car.DoesNotExist as e:
        print('Car with pk not found!!', e)
        return redirect(reverse('cars:list'))
