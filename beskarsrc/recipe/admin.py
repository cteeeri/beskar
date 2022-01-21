from django.contrib import admin
from recipe.models import Ingredient
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'freshnesslevel')

admin.site.register(Ingredient, RecipeAdmin)

