from django.shortcuts import render, redirect
from .models import BuildingType, Town, Building
from django.db.models import Sum, F
from .forms import BuildingForm

# Create your views here.


def town(request):
    user_town = (Town.objects.filter(character__user=request.user))
    building_list = Building.objects.filter(building_type__building__town__character__user=request.user)
#    get defence sum of all buildings. You get dict, then you get value and transform it into list
    defence = list((BuildingType.objects.filter(building__town__character__user=request.user)
                    .aggregate(Sum(F('defence')))).values())[0]

    if request.method == "POST":
        form = BuildingForm(request.POST)
        if form.is_valid():
            ap = form.save(commit=False)
            ap.save()
            return redirect('town/town.html')
    else:
        form = BuildingForm()

    return render(request, 'town/town.html', {'user_town': user_town,
                                              'building_list': building_list,
                                              'defence': defence,
                                              'form': form})
