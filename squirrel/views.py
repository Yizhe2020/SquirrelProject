from django.http import HttpResponse
from django.shortcuts import render
from .models import Data

def home_page(request):
    squirrels = 'Squirrel Tracker'
    return render(request,'squirrel/index.html',{'Squirrels': squirrels})

def map(request):
    plot = Data.objects.all()[:100]
    return render(request,'squirrel/map.html',{'Plot': plot})
# Create your views here.
