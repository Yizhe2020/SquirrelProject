from django.urls import path

from . import views

app_name = 'squirrel'

urlpatterns = [
    path('', views.home_page, name = 'index'),
    path('map/', views.map, name = 'map'),
    path('sightings/', views.sightings, name = 'sightings'),
    path('sightings/add/', views.create_sightings, name = 'create_sightings'),
    path('sightings/stats/', views.stats, name = 'stats'),
    path('sightings/<Unique_Squirrel_ID>/', views.update_sightings, name = 'update_sightings'),
]
