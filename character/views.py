from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .form import CharacterForm
from town.models import Town
# Create your views here.


def create_character(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            name = form.save(commit=False)
            name.user = request.user
            name.save()
            return redirect('index.html')
    else:
        form = CharacterForm()
    return render(request, 'character/create.html', {'form': form, })


def index(request):
    character_names = (Character.objects.filter(user=request.user).values_list('name', flat=True))[0]
    town_id = (Character.objects.filter(user=request.user).values_list('town_id', flat=True))
    town_list = (Town.objects.filter(id=town_id).values_list('name', flat=True))[0]
    return render(request, 'character/index.html', {'character_names': character_names, 'town_list': town_list})

