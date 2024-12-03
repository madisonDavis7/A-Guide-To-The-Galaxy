from django.db import models
from django.urls import reverse
from star_ratings.models import Rating

class StarTour(models.Model):
    name = models.CharField(max_length=100) #name of Star
    type = models.CharField(max_length=100) #Star Type
    distance = models.CharField(max_length=100) #Distance in light years from Earth
    temp = models.CharField(max_length=100) #Surface Temperature of Star

    about1 = models.CharField(max_length=200) #First  about bullet
    about2 = models.CharField(max_length=200) #Second about bullet
    about3 = models.CharField(max_length=200) #Third  about bullet

    length = models.PositiveIntegerField() #length in days
    num_people = models.PositiveIntegerField() #num of people who can go

    def __str__(self):
        return self.name

class ConstellationTour(models.Model):
    name = models.CharField(max_length=100) #name of Star
    stars = models.CharField(max_length=100) #Notable stars within constellation
    #starnum = models.CharField(max_length=10) #Number of stars in the constellation

    about1 = models.CharField(max_length=200) #First  about bullet
    about2 = models.CharField(max_length=200) #Second about bullet
    about3 = models.CharField(max_length=200) #Third  about bullet

    length = models.PositiveIntegerField() #length in days
    num_people = models.PositiveIntegerField() #num of people who can go

    def __str__(self):
        return self.name