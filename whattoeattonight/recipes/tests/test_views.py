from django.urls import reverse
from django.test import TestCase

from recipes.models import Recipe

# TODO add more tests for all views, models and forms


class TestRecipeIndexViewTestCase(TestCase):

    def create_recipe(self):
        """
        Create a recipe with the given name, description, step and portions.
        Check that the names are properly saved.
        """
        recipe1 = Recipe(name="Chicken Soup", description="Delicious chicken soup", steps="Step 1", portions=1,
                         duration=1)
        recipe2 = Recipe(name="Beef Soup", description="Delicious beef soup", steps="Step 1", portions=1, duration=1)
        self.assertEqual(recipe1.name, "Chicken Soup")
        self.assertEqual(recipe2.name, "Beef Soup")

    def test_no_recipes(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("recipes:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No recipes are available.")
