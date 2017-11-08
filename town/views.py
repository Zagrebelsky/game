from django.shortcuts import render
from .models import Building, BuildingType
from character.models import Character

# Create your views here.


def town(request):
    town_id = (Character.objects.filter(user=request.user).values_list('town_id', flat=True))
    building_id = (Building.objects.filter(town_id=town_id).values_list('building_type_id', flat=True))
    building_list = (BuildingType.objects.filter(id=building_id).values_list('name', flat=True))[0]
    return render(request, 'town/town.html', {'building_list': building_list})
