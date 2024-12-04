'''
import requests
from django.shortcuts import render
from django.templatetags.static import static
import json
from django.conf import settings


def home(request):
    nasa_api_key = 'YOUR_NASA_API_KEY'  # Replace with your actual NASA API key
    url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}'

    # Make a request to NASA API
    response = requests.get(url)
    data = response.json()

    # Extract the relevant information from the API response
    image_url = data['url']
    image_title = data['title']
    image_explanation = data['explanation']

    # Render the home page with the image data
    return render(request, 'home.html', {
        'image_url': image_url,
        'image_title': image_title,
        'image_explanation': image_explanation,
    })


def home_view(request):
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key='+settings.NASA_API_KEY)
    loaded_json = json.loads(response.text)

    daily_image = loaded_json.get('url')
    title = loaded_json.get('title')
    explanation = loaded_json.get('explanation')
    date = loaded_json.get('date')
    owner = loaded_json.get('copyright')

    context = {
        'daily_image': daily_image,
        'title':title,
        'explanation':explanation,
        'date':date,
        'owner':owner
    }

    return render(request, "home.html", context)

'''
from django.shortcuts import render
from datetime import datetime
import requests
from django.templatetags.static import static  # Import this to use static files

NASA_API_URL = 'https://api.nasa.gov/planetary/apod'
NASA_API_KEY = 'xgbprF9SyPJs5cFNUXfbeQi8A7F2yVFZYIg2xcxw'

def home(request):
    # Get NASA APOD data
    try:
        nasa_data = get_nasa_apod()
        #print("NASA Data: ", nasa_data)  # Debugging print
    except Exception as e:
        print("Error: ", e)
        nasa_data = {}

    # Extract relevant information
    title = nasa_data.get("title", "No Title")
    img_url = nasa_data.get("url", "")  # Use a fallback if no URL

    # Check if the URL is a video
    if not img_url.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # Not an image
        # Use a static fallback image if it's a video
        img_url = static('images/fallback.jpg')  # This should be the path to your fallback image in static/images/

    # Format the date for readability
    date_object = datetime.strptime(nasa_data.get("date", "2024-01-01"), "%Y-%m-%d")
    formatted_date = date_object.strftime("%B %d, %Y")

    # Prepare the context dictionary
    context = {
        "url": img_url,
        "date": formatted_date,
        "title": title,
    }

    print("Context: ", context)  # Debugging print to check what we're passing to the template
    return render(request, "home.html", context)
    
# Get Astronomy Picture of the Day from NASA API
def get_nasa_apod():
    response = requests.get(NASA_API_URL, params={"api_key": NASA_API_KEY})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error: Failed to retrieve Astronomy Picture of the Day")
