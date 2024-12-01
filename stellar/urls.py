from django.urls import path
from .views import StellarHomeView

urlpatterns = [
    path("", StellarHomeView.as_view(), name="stellarHome")
]