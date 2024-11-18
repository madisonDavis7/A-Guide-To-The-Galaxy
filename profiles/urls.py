from django.urls import path

from .views import (
	SpaceTravelerProfileCreateView,
	SpaceTravelerProfileUpdateView,
	SpaceTravelerProfileViewView
)

app_name = 'profiles'
urlpatterns = [
	path('create/', SpaceTravelerProfileCreateView.as_view(), name='create'),
	path('<int:pk>/', SpaceTravelerProfileViewView.as_view(), name='view_profile'),
	path('<int:pk>/update', SpaceTravelerProfileUpdateView.as_view(), name='update'),
]
