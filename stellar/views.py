from django.views.generic import TemplateView, DetailView
from .models import StarTour, ConstellationTour
from django.views import View
from django.urls import reverse_lazy, reverse

# Create your views here.
class StellarHomeView(TemplateView):
    template_name = "stellar.html"

class StarTourView(DetailView):
    model = StarTour
    template_name = 'star.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star tours"] = StarTour.objects.all()
        return context
    
class ConstellationTourView(DetailView):
    model = ConstellationTour
    template_name = 'constellation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["constellation tour"] = ConstellationTour.objects.all()
        return context
    
    