from dataclasses import fields
from django.db import models

# Create your models here.

class FreshnessLevel(models.TextChoices):
    FRESH = 'FRESH'
    DRIED = 'DRIED'
    FERMENTED = 'FERMENTED'


class Ingredient(models.Model):
    name = models.CharField(max_length=30, unique=True)
    freshnesslevel = models.CharField(max_length=20, choices=FreshnessLevel.choices, default=FreshnessLevel.FRESH)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'freshnesslevel'], name='ingredient freshness level')
        ]





