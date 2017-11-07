from django.contrib import admin
from .models import Character, Inventory


# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    model = Character


class InventoryAdmin(admin.ModelAdmin):
    model = Inventory


admin.site.register(Character, CharacterAdmin)
admin.site.register(Inventory, InventoryAdmin)
