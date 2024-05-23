from django.shortcuts import render
from django.http import HttpRequest
from .models import Patient

# Create your views here.
def list_patients(request: HttpRequest):
    all_patients = Patient.objects.all()
    return render(request, 'office/list.html', context={'patients': all_patients})