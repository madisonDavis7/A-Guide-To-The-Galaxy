from django.shortcuts import render, get_object_or_404
from .models import PlanetaryTour

def planetary(request):
    return render(request, 'planetary/planetary.html')

def mercury_page(request):
    mercury_tour = get_object_or_404(PlanetaryTour, name="Mercury Tour")

    return render(request, 'planetary/mercury_page.html', {'tour': mercury_tour, })

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

    return render(request, 'planetary/sedna_page.html', {'tour': sedna_tour})
