"""
Data migration to add stellar tours to production database
"""
from django.db import migrations

def add_stellar_tours(apps, schema_editor):
    StarTour = apps.get_model('stellar', 'StarTour')
    
    star_tours = [
        {
            'name': 'Betelgeuse',
            'type': 'Red Supergiant',
            'distance': '640',
            'temp': '3,500',
            'home_image': 'static/Betelgeuse.jpg',
            'image1': 'static/Betelgeuse.jpg',
            'image2': 'static/Betelgeuse.jpg',
            'image3': 'static/Betelgeuse.jpg',
            'about1': 'One of the largest known stars in the Milky Way galaxy.',
            'about2': 'A red supergiant star in the constellation Orion.',
            'about3': 'Expected to explode as a supernova within the next 100,000 years.',
            'link': 'https://www.nasa.gov/feature/goddard/2020/hubble-sees-star-betelgeuse-slowly-recovering-after-blowing-its-top',
            'length': 12,
            'num_people': 25
        },
        {
            'name': 'Sirius',
            'type': 'Main Sequence',
            'distance': '8.6',
            'temp': '9,940',
            'home_image': 'static/sirius.jpg',
            'image1': 'static/sirius.jpg',
            'image2': 'static/SiriusCompare.jpg',
            'image3': 'static/SiriusQuality.jpg',
            'about1': 'The brightest star in the Earth night sky.',
            'about2': 'A binary star system in the constellation Canis Major.',
            'about3': 'Has a white dwarf companion star called Sirius B.',
            'link': 'https://www.nasa.gov/mission_pages/hubble/science/sirius.html',
            'length': 6,
            'num_people': 20
        }
    ]
    
    for tour_data in star_tours:
        StarTour.objects.get_or_create(name=tour_data['name'], defaults=tour_data)

def reverse_stellar_tours(apps, schema_editor):
    StarTour = apps.get_model('stellar', 'StarTour')
    StarTour.objects.filter(name__in=['Betelgeuse', 'Sirius']).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('stellar', '0005_constellationtour_home_image_startour_home_image'),
    ]

    operations = [
        migrations.RunPython(add_stellar_tours, reverse_stellar_tours),
    ]
