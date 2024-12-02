from django.test import TestCase
from django.urls import reverse
from .models import PlanetaryTour

class PlanetaryTourModelTest(TestCase):

    def test_planetary_tour_creation(self):

        tour = PlanetaryTour.objects.create (
            name = "Mars Tour", 
            length = 10, 
            num_people = 45
        )

        self.assertEqual(tour.name, "Mars Tour")
        self.assertEqual(tour.length, 10)
        self.assertEqual(tour.num_people, 45)

    def test_planetary_tour_str_method(self):

        tour = PlanetaryTour.objects.create (
            name = "Mars Tour", 
            length = 10,
            num_people = 45
        )

        self.assertEqual(str(tour), "Mars Tour")

class PlanetaryViewTests(TestCase):
    def test_planetary_views(self):
        url = reverse('planetary')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planetary/planetary.html')

class MercuryPageView(TestCase):
    def setUp(self):
        PlanetaryTour.objects.create(
            name="Mercury Tour",
            length = 10, 
            num_people = 50
        )
    
    def test_mercury_page_view(self):
        url = reverse('mercury_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planetary/mercury_page.html')

        self.assertIn('tour', response.context)
        self.assertEqual(response.context['tour'].name, "Mercury Tour")
        self.assertEqual(response.context['tour'].length, 10)
        self.assertEqual(response.context['tour'].num_people, 50)

class MarsPageView(TestCase):
    def setUp(self):
        PlanetaryTour.objects.create(
            name="Mars Tour",
            length = 12, 
            num_people = 45
        )
    
    def test_mars_page_view(self):
        url = reverse('mars_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planetary/mars_page.html')

        self.assertIn('tour', response.context)
        self.assertEqual(response.context['tour'].name, "Mars Tour")
        self.assertEqual(response.context['tour'].length, 12)
        self.assertEqual(response.context['tour'].num_people, 45)

class NeptunePageView(TestCase):
    def setUp(self):
        PlanetaryTour.objects.create(
            name="Neptune Tour",
            length = 12, 
            num_people = 45
        )
    
    def test_neptune_page_view(self):
        url = reverse('neptune_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planetary/neptune_page.html')

        self.assertIn('tour', response.context)
        self.assertEqual(response.context['tour'].name, "Neptune Tour")
        self.assertEqual(response.context['tour'].length, 12)
        self.assertEqual(response.context['tour'].num_people, 45)

class PlutoPageView(TestCase):
    def setUp(self):
        PlanetaryTour.objects.create(
            name="Pluto Tour",
            length = 12, 
            num_people = 45
        )
    
    def test_pluto_page_view(self):
        url = reverse('pluto_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planetary/pluto_page.html')

        self.assertIn('tour', response.context)
        self.assertEqual(response.context['tour'].name, "Pluto Tour")
        self.assertEqual(response.context['tour'].length, 12)
        self.assertEqual(response.context['tour'].num_people, 45)

class KeplerPageView(TestCase):
    def setUp(self):
        PlanetaryTour.objects.create(
            name="Kepler Tour",
            length = 12, 
            num_people = 45
        )
    
    def test_kepler_page_view(self):
        url = reverse('kepler_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planetary/kepler_page.html')

        self.assertIn('tour', response.context)
        self.assertEqual(response.context['tour'].name, "Kepler Tour")
        self.assertEqual(response.context['tour'].length, 12)
        self.assertEqual(response.context['tour'].num_people, 45)

class SednaPageView(TestCase):
    def setUp(self):
        PlanetaryTour.objects.create(
            name="Sedna Tour",
            length = 12, 
            num_people = 45
        )
    
    def test_sedna_page_view(self):
        url = reverse('sedna_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planetary/sedna_page.html')

        self.assertIn('tour', response.context)
        self.assertEqual(response.context['tour'].name, "Sedna Tour")
        self.assertEqual(response.context['tour'].length, 12)
        self.assertEqual(response.context['tour'].num_people, 45)





