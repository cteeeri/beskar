from django.contrib import admin
from recipe.models import Recipe, Foodtags,Cooking_Instruction,Food_Item, Ingredient_Preparation
# Register your models here.

# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'freshnesslevel')

admin.site.register(Recipe)
admin.site.register(Foodtags)
admin.site.register(Cooking_Instruction)
admin.site.register(Food_Item)
admin.site.register(Ingredient_Preparation)

