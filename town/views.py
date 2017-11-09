from django.shortcuts import render
from .models import BuildingType, Town, Building
from django.db.models import Sum, F

# Create your views here.


def town(request):
    town_name = (Town.objects.filter(character__user=request.user).values_list('name', flat=True))[0]
    building_list = (BuildingType.objects.filter(building__town__character__user=request.user).values_list('name', flat=True))
    building_ap = list(Building.objects.filter(town__character__user=request.user).values_list('ap', flat=True))
#    get defence sum of all buildings. You get dict, then you get value and transform it into list
    defence = list((BuildingType.objects.filter(building__town__character__user=request.user).aggregate(Sum(F('defence')))).values())[0]
    return render(request, 'town/town.html', {'town_name': town_name,
                                              'building_list': building_list,
                                              'building_ap': building_ap,
                                              'defence': defence, })
