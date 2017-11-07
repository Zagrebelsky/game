from django.db import models


# Create your models here.


class Town(models.Model):
    name = models.CharField(max_length=200)
    citizens = models.IntegerField(default=40)

    def __str__(self):
        return self.name


class BuildingType(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Building(models.Model):
    town = models.ForeignKey('town.Town', on_delete=models.CASCADE)
    building_type = models.ForeignKey('town.BuildingType', on_delete=models.CASCADE)
    success = models.BooleanField(default=False)
    ap = models.IntegerField(default=0)
