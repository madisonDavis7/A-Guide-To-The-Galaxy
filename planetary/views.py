from django.shortcuts import render

def planetary(request):
    return render(request, 'planetary/planetary.html')

def mercury_page(request):
    return render(request, 'planetary/mercury_page.html')

def mars_page(request):
    return render(request, 'planetary/mars_page.html')

def neptune_page(request):
    return render(request, 'planetary/neptune_page.html')

def pluto_page(request):
    return render(request, 'planetary/pluto_page.html')

def kepler_page(request):
    return render(request, 'planetary/depler_page.html')

def sedna_page(request):
    return render(request, 'planetary/sedna.html')

