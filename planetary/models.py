from django.db import models
from star_ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

class PlanetaryTour(models.Model):
    name = models.CharField(max_length=100) #name of tour
    length = models.PositiveIntegerField() #length in days
    num_people = models.PositiveIntegerField() #num of people who can go

    #allows access to ratings for each tour
    ratings = GenericRelation(Rating)

    #avg rating for tour
    def avg_rating(self):
        return self.ratings.aggregate(models.Avg('average'))['average__avg'] or 0
    
    def __str__(self):
        return self.name


