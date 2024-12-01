from django.db import models
from star_ratings.models import Rating


class PlanetaryTour(models.Model):
    name = models.CharField(max_length=100) #name of tour
    length = models.PositiveIntegerField() #length in days
    num_people = models.PositiveIntegerField() #num of people who can go

    def __str__(self):
        return self.name
    


