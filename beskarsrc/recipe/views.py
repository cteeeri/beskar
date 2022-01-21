from django.shortcuts import render
from django.views import generic

from recipe.models import Ingredient
# Create your views here.


class IngredientListView(generic.ListView):
    model = Ingredient



