# Generated by Django 4.2 on 2023-11-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Ingredient")),
                (
                    "measuring_unit",
                    models.TextField(
                        choices=[
                            ("g", "grams"),
                            ("l", "liters"),
                            ("ml", "milliliters"),
                            ("kg", "kilograms"),
                        ],
                        verbose_name="Measuring Unit",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Recipe name")),
                (
                    "description",
                    models.TextField(max_length=500, verbose_name="Description"),
                ),
                ("steps", models.TextField(max_length=2000, verbose_name="Steps")),
                (
                    "portions",
                    models.IntegerField(
                        verbose_name="Approximate of resulted portions"
                    ),
                ),
                (
                    "duration",
                    models.FloatField(verbose_name="Approximate time of preparation"),
                ),
                ("ingredients", models.ManyToManyField(to="recipes.ingredient")),
            ],
        ),
    ]
