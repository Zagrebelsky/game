from django.contrib import admin
from .models import Town, BuildingType


# Register your models here.


class TownAdmin(admin.ModelAdmin):
    model = Town


class BuildingTypeAdmin(admin.ModelAdmin):
    model = BuildingType


admin.site.register(Town, TownAdmin)
admin.site.register(BuildingType, BuildingTypeAdmin)
