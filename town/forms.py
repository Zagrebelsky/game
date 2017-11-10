from django import forms
from .models import Building


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ('ap', 'building_type', 'town')
