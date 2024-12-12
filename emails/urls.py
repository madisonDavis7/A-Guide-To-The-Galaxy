from django.urls import path

from .views import (
	WelcomeView
)

app_name = 'emails'
urlpatterns = [
	path('welcome/', WelcomeView.as_view())
]
