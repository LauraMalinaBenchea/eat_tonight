from django.db import models
from .constants import measuring_units


class Ingredient(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ingredient")
    measuring_unit = models.TextField(choices=measuring_units, verbose_name="Measuring Unit")

    def __str__(self):
        return self.name

# TODO consider cooking methods?


# TODO fix recipe reference to ingredients
class Recipe(models.Model):
    name = models.CharField(max_length=200, verbose_name="Recipe name")
    description = models.TextField(max_length=500, verbose_name="Description")
    ingredients = models.ManyToManyField(to=Ingredient)
    steps = models.TextField(max_length=2000, verbose_name="Steps")
    portions = models.IntegerField(verbose_name="Approximate of resulted portions")
    duration = models.FloatField(verbose_name="Approximate time of preparation")
    # photo = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name




