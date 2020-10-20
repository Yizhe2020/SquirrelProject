from django.http import HttpResponse
from django.shortcuts import render
from .models import Data
from .form import UpdateForm, CreateForm

def home_page(request):
    squirrels = 'Squirrel Tracker'
    return render(request,'squirrel/index.html',{'Squirrels': squirrels})

def map(request):
    plot = Data.objects.all()[:100]
    return render(request,'squirrel/map.html',{'Plot': plot})

def sightings(request):
    squirrels = Data.objects.all()
    return render(request,'squirrel/sightingslist.html',{'Squirrel': squirrels})

def update_sightings(request, Unique_Squirrel_ID):
    squirrels = Data.objects.get(Unique_Squirrel_ID = Unique_Squirrel_ID)
    if request.method == 'POST':
        form = UpdateForm(request.POST)
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
    PM_Count = squirrels.filter(Shift = 'PM').count()
    Cinnamon_Count = squirrels.filter(Primary_Fur_Color = 'Cinnamon').count()
    Eating_Count = squirrels.filter(Eating = 'True').count()
    Moans_Count = squirrels.filter(Moans = 'True').count()
    Indifferent_Count = squirrels.filter(Indifferent = 'True').count()
    return render(request,'squirrel/stats.html', {'PM_Count': PM_Count, 'Cinnamon_Count': Cinnamon_Count, 'Eating_Count': Eating_Count,
        'Moans_Count': Moans_Count, 'Indifferent_Count': Indifferent_Count})


# Create your views here.
