from dataclasses import fields
import uuid
from django.db import models

# Create your models here.



class Food_Item(models.Model):
    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return f'{self.name}'


    
class Foodtags(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Enter a food tags (e.g. dinner, Vegan, Spicy etc.)",
        blank=False
        )

    def __str__(self):
        return self.name





import uuid

class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular recipe")
    name = models.CharField(max_length=40, blank=False)
    # By = 
    short_narrative = models.TextField(max_length=1000, help_text="Brief narrative for recipe.")
    yield_serving = models.CharField(max_length=4)
    prep_time = models.CharField(max_length=20)
    # cooking_instruction = models.ForeignKey(Cooking_Instruction, on_delete=models.CASCADE)
    recently_edited = models.DateTimeField()
    short_warning = models.TextField()
    # ingredient_details = models.ForeignKey(IngredientDetails, on_delete=models.CASCADE)
    foodtags = models.ManyToManyField(Foodtags, help_text="Any food tags for this recipe?", related_name="foodtags")
    # image = 

    def __str__(self):
        return f'{self.foodtags} {self.name} {self.short_narrative[:20]}...'



class Cooking_Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_number = models.IntegerField()
    instruction = models.TextField(max_length=40)
    # image = 

    def __str__(self):
        return f'step {self.step_number}, {self.instruction} '


class Ingredient_Preparation(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    food_item = models.ForeignKey(Food_Item,on_delete=models.CASCADE)
    # image = 
    amount = models.CharField(max_length=20)
    prep_instruction = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.amount} {self.food_item} {self.prep_instruction[:20]}...'



