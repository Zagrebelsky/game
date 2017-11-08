from django.shortcuts import render
from .models import BuildingType, Town
from character.models import Character

# Create your views here.


def town(request):
    town_name = (Town.objects.filter(character__user=request.user).values_list('name', flat=True))[0]
    building_list = (BuildingType.objects.filter(building__town__character__user=request.user).values_list('name', flat=True))[0]
    return render(request, 'town/town.html', {'town_name': town_name, 'building_list': building_list})
