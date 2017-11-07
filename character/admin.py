from django.contrib import admin
from .models import Character


# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    model = Character


admin.site.register(Character, CharacterAdmin)
