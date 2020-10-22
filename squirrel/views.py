from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import Data
from .forms import UpdateForm, CreateForm

def home_page(request):
    squirrels = 'Squirrel Tracker'
    return render(request,'squirrel/index.html',{'Squirrels': squirrels})

def map(request):
    plot = Data.objects.all()[:100]
    return render(request,'squirrel/map.html',{'Plot': plot})

def sightings(request):
    squirrels = Data.objects.all()
    return render(request,'squirrel/sightingslist.html',{'Squirrel': squirrels})

def update_sightings(request,Unique_Squirrel_ID):
    squirrels = Data.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance = squirrels)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = UpdateForm(instance = squirrels)
    return render(request,'squirrel/update_sightings.html', {'Form': form})

def create_sightings(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = CreateForm()
    return render(request,'squirrel/create_sightings.html',{'Form': form})

def stats(request):
    squirrels = Data.objects.all()
    AM_Count = squirrels.filter(Shift = "AM").count()
    PM_Count = squirrels.filter(Shift = 'PM').count()
    Total = AM_Count+PM_Count
    Cinnamon_Count = squirrels.filter(Primary_Fur_Color = 'Cinnamon').count()
    Eating_Count = squirrels.filter(Eating = 'True').count()
    Moans_Count = squirrels.filter(Moans = 'True').count()
    Indifferent_Count = squirrels.filter(Indifferent = 'True').count()
    return render(request,'squirrel/stats.html', {"AM_Count": AM_Count, 'PM_Count': PM_Count, 'Cinnamon_Count': Cinnamon_Count, 'Eating_Count': Eating_Count,
        'Moans_Count': Moans_Count, 'Indifferent_Count': Indifferent_Count,'Total':Total})


# Create your views here.
