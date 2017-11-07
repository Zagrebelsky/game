from django.db import models

# Create your models here.


class Character(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    action_points = models.IntegerField(default=6)
    town = models.ForeignKey('town.Town', default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name


