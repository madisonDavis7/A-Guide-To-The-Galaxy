import requests
from django.shortcuts import render
from django.conf import settings

def home(request):
    # Set the NASA API key from settings.py
    api_key = settings.NASA_API_KEY
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

    # Fetch the data from NASA API
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an exception for bad HTTP responses (e.g., 404 or 500)
        data = response.json()

        # Extract image or video URL and metadata from the response
        image_url = data.get('url')
        media_type = data.get('media_type')  # This could be 'image' or 'video'
        title = data.get('title')
        explanation = data.get('explanation')

        # If it's a video, use the same image URL
        if media_type == 'video':
            image_url = data.get('hdurl', image_url)  # Use hdurl if it's available for videos

        # Pass the data to the template context
        context = {
            'image_url': image_url,
            'media_type': media_type,
            'title': title,
            'explanation': explanation,
        }

    except requests.exceptions.RequestException as e:
        # In case of an error, you can pass an error message to the template
        context = {
            'error_message': 'Could not fetch NASA Picture of the Day. Please try again later.',
        }

    return render(request, 'home.html', context)

