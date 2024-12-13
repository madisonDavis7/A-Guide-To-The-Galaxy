from django.test import TestCase
from django.urls import reverse
from .models import StarTour
from .models import ConstellationTour

# Create your tests here.
class StellarTourModelTest(TestCase):

    def test_star_tour(self):

        tour = StarTour.objects.create (
            name = "Sirius Tour", 
            length = 10, 
            num_people = 45
        )

        self.assertEqual(tour.name, "Sirius Tour")
        self.assertEqual(tour.length, 10)
        self.assertEqual(tour.num_people, 45)

    def test_constellation_tour(self):

        tour = ConstellationTour.objects.create (
            name = "Orion Tour", 
            length = 10,
            num_people = 45
        )

        self.assertEqual(tour.name, "Orion Tour")
        self.assertEqual(tour.length, 10)
        self.assertEqual(tour.num_people, 45)