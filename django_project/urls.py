"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from . import views
from .views import HomepageView, SignupView
<<<<<<< HEAD
from .views import planetary
=======
from .views import stellar
>>>>>>> 63b1da7355e1fa8c4ed713d0512886517cc6ca87

urlpatterns = [
	path('admin/', admin.site.urls),
	
	# search our auth stuff first, then pass the rest off to the base libs
	path('accounts/', include('accounts.urls')),
	path('accounts/', include('allauth.urls')),
	path('accounts/', include('django.contrib.auth.urls')),

	path('profiles/', include('profiles.urls')),
	path('planetary/', include('planetary.urls')),
	path('', HomepageView.as_view(), name='home'),
<<<<<<< HEAD
	path('planetary/', planetary, name='planetary'),
	path('stellar/', include("stellar.urls")),
=======
	path('stellar/', stellar, name='stellar'),
>>>>>>> 63b1da7355e1fa8c4ed713d0512886517cc6ca87
	#path('', SignupView.as_view(), name='signup'),
	path('ratings/', include('star_ratings.urls', namespace='ratings')),

]


if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path(r'^__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns
