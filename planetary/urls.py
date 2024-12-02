from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.planetary, name="planetary"),
    path('tours/<int:pk>/')
    path('mercury/', views.mercury_page, name="mercury_page"),
    path('mars/', views.mars_page, name="mars_page"),
    path('neptune/', views.neptune_page, name="neptune_page"),
    path('pluto/', views.pluto_page, name="pluto_page"),
    path('kepler/', views.kepler_page, name="kepler_page"),
    path('sedna/', views.sedna_page, name="sedna_page"),
	path('tour/<int:pk>/', views.PlanetaryTourView.as_view())
    # path('mercury/', views.mercury_page, name="mercury_page"),
    # path('mars/', views.mars_page, name="mars_page"),
    # path('neptune/', views.neptune_page, name="neptune_page"),
    # path('pluto/', views.pluto_page, name="pluto_page"),
    # path('kepler/', views.kepler_page, name="kepler_page"),
    # path('sedna/', views.sedna_page, name="sedna_page"),

]