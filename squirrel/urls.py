from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name = 'index'),
    path('map/', views.map, name = 'map'),
    path('sightings/', views.sightings, name = 'sightings'),
]
