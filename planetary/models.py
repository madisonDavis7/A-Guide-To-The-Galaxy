from django.db import models



class PlanetaryTour(models.Model):
    location_and_orbit = models.TextField()
    about_planet = models.TextField()
    name = models.CharField(max_length=100) #name of tour
    length = models.PositiveIntegerField() #length in days
    num_people = models.PositiveIntegerField() #num of people who can go
    image = models.ImageField(upload_to='planetary_tours/', blank=True, null=True)  # Add this line to store images


    def __str__(self):
        return self.name
    


