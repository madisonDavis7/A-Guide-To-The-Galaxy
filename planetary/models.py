from django.db import models
from star_ratings.models import Rating

class PlanetaryTour(models.Model):
    name = models.CharField(max_length=100) #name of tour
    length = models.PositiveIntegerField() #length in days
    num_people = models.PositiveIntegerField() #num of people who can go

    ratings = models.ManyToManyField(Rating, related_name="planetary_tours", blank=True)


