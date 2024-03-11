from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class food_item(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protiens = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()


class consume(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(food_item, on_delete=models.CASCADE)
