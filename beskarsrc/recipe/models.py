from dataclasses import fields
from django.db import models

# Create your models here.

class FreshnessLevel(models.TextChoices):
    FRESH = 'Fresh'
    DRIED = 'Dried'
    FERMENTED = 'Fermented'
    PICKLED = 'Pickled'

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    freshnesslevel = models.CharField(max_length=20, choices=FreshnessLevel.choices, default=FreshnessLevel.FRESH)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'freshnesslevel'], name='ingredient_freshness_level')
        ]

    def __str__(self):
        return f'{self.name} {self.freshnesslevel}'
    
