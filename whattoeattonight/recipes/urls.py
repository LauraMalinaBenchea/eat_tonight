from django.urls import path
from . import views


app_name = "recipes"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>", views.RecipeDetailView.as_view(), name="detail"),
    path("<int:pk>/update", views.RecipeUpdateView.as_view(), name="update"),
    path("new", views.AddRecipeView.as_view(), name="add_recipe"),
]
