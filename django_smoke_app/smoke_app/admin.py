from django.contrib import admin
from .models import Strain, CategoryStrain, CountersByEffect, CountersByFlavors

# Register your models here.
admin.site.register(Strain)
