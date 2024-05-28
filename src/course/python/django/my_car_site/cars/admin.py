from django.contrib import admin
from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin): # type: ignore
    """
    Admin class for Car model. Gives more control over the admin page.
    """
    # fields = ['brand', 'year']
    fieldsets = [
        ('TIME INFORMATION', {'fields': ['year']}),
        ('CAR INFORMATION', {'fields': ['brand']}),
    ]

admin.site.register(Car, CarAdmin)
