from django.views.generic import TemplateView

# Create your views here.
class StellarHomeView(TemplateView):
    template_name = "stellar.html"