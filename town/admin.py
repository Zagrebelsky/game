from django.contrib import admin
from .models import Town, BuildingType, Building


# Register your models here.


class TownAdmin(admin.ModelAdmin):
    model = Town


class BuildingTypeAdmin(admin.ModelAdmin):
    model = BuildingType


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('town_id', 'building_type', 'success', 'ap')

admin.site.register(Town, TownAdmin)
admin.site.register(BuildingType, BuildingTypeAdmin)
admin.site.register(Building, BuildingAdmin)
