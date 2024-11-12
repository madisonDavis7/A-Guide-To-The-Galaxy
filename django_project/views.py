#django_project/ view.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')