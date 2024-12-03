from django.contrib import admin
from .models import StarTour, ConstellationTour

class StarTourAdmin(admin.ModelAdmin):
    model = StarTour
    list_display = (
        'name', 
        'type', 
        'distance', 
        'temp', 
        'length', 
        'about1',
        'about2',
        'about3',
        'num_people')
    
class ConstellationTourAdmin(admin.ModelAdmin):
    model = ConstellationTour
    list_display = (
        'name', 
        'stars', 
        #'starnum',
        'length', 
        'about1',
        'about2',
        'about3',
        'num_people')

admin.site.register(StarTour)
admin.site.register(ConstellationTour)