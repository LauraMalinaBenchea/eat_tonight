from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Recipe
from .forms import RecipeBaseForm


class IndexView(generic.ListView):
    template_name = "recipes/index.html"
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    context_object_name = 'recipes'

    model = Recipe

    def get_queryset(self):
        print(self.recipes)
        return self.recipes


class AddRecipeView(generic.CreateView):
    model = Recipe
    template_name = "recipes/add_recipe.html"
    form_class = RecipeBaseForm

    success_url = reverse_lazy('recipes:index')


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = "recipes/detail.html"


class RecipeUpdateView(generic.UpdateView):
    model = Recipe
    template_name = "recipes/update.html"
