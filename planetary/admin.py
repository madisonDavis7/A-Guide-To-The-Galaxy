from django.contrib import admin
from .models import PlanetaryTour

class PlanetaryTourAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'num_people')