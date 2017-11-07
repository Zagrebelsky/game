from django.db import models


# Create your models here.


class Town(models.Model):
    name = models.CharField(max_length=200)
    citizens = models.IntegerField(default=40)
    wall = models.BooleanField(default=False)
    wall_ap = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class BuildingType(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name
