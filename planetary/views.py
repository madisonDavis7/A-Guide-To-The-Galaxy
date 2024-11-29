from django.shortcuts import render, get_object_or_404
from .models import PlanetaryTour
from star_ratings.models import Rating
from django.db.models import Avg
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
import json

def planetary(request):
    return render(request, 'planetary/planetary.html')

def get_average_rating(tour):
    avg_rating = Rating.objects.filter(content_object=tour).aggregate(Avg('average'))['average__avg'] or 0
    return avg_rating

def mercury_page(request):
    mercury_tour = get_object_or_404(PlanetaryTour, name="Mercury Tour")
    average_rating = mercury_tour.avg_rating()
    return render(request, 'planetary/mercury_page.html', {'tour': mercury_tour, 'average_rating': average_rating})

def mars_page(request):
    mars_tour = get_object_or_404(PlanetaryTour, name="Mars Tour")
    return render(request, 'planetary/mars_page.html', {'tour': mars_tour})

def neptune_page(request):
    neptune_tour = get_object_or_404(PlanetaryTour, name="Neptune Tour")
    return render(request, 'planetary/neptune_page.html', {'tour': neptune_tour})

def pluto_page(request):
    pluto_tour = get_object_or_404(PlanetaryTour, name="Pluto Tour")
    return render(request, 'planetary/pluto_page.html', {'tour': pluto_tour})

def kepler_page(request):
    kepler_tour = get_object_or_404(PlanetaryTour, name="Kepler Tour")
    return render(request, 'planetary/kepler_page.html', {'tour': kepler_tour})

def sedna_page(request):
    sedna_tour = get_object_or_404(PlanetaryTour, name="Sedna Tour")
    return render(request, 'planetary/mars_page.html', {'tour': sedna_tour})

def rate_tour(request, tour_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        rating_value = data.get('rating')

        # Get the specific tour object
        tour = get_object_or_404(PlanetaryTour, id=tour_id)

        # Create or update the rating for the specific tour
        content_type = ContentType.objects.get_for_model(tour)
        Rating.objects.update_or_create(
            content_type=content_type,
            object_id=tour.id,
            defaults={'value': rating_value}
        )
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False}, status=400)
