from django.db import models
from item.models import Item
# Create your models here.


class Character(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    action_points = models.IntegerField(default=6)
    town = models.ForeignKey('town.Town', default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    character = models.ForeignKey('character.Character', on_delete=models.CASCADE)
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)

