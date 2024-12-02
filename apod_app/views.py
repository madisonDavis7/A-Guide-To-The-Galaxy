import requests
from django.shortcuts import render

def apod_view(request):
    api_key = 'xgbprF9SyPJs5cFNUXfbeQi8A7F2yVFZYIg2xcxw'  
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

    # Make the GET request to the NASA API
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()

        # Extract data from the response
        apod_image_url = data['url']
        apod_title = data['title']
        apod_description = data['explanation']
        media_type = data['media_type']

        # Add the print statement to output the image URL
        print(f"APOD Image URL: {apod_image_url}")

        if media_type == 'video':
            apod_image_url = None  # Set to None if it's a video
            apod_video_url = data['url'] 
        else:
            apod_video_url = None
    else:
        apod_image_url = None
        apod_video_url = None
        apod_title = "Error"
        apod_description = "Unable to fetch Astronomy Picture of the Day."

    # Pass data to template
    return render(request, 'apod_app/apod.html', {
        'apod_image_url': apod_image_url,
        'apod_video_url': apod_video_url,
        'apod_title': apod_title,
        'apod_description': apod_description,
    })

