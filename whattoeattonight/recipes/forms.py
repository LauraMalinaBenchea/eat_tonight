from django import forms

from .models import Ingredient, Recipe


class RecipeBaseForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        required=True,
        label="Ingredients",
        widget=forms.CheckboxSelectMultiple,
        queryset=Ingredient.objects.all(),
    )

    class Meta:
        model = Recipe

        fields = [
            "name",
            "description",
            "ingredients",
            "steps",
            "portions",
            "duration",
        ]
