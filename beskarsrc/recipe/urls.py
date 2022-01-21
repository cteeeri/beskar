from django.urls import path
from recipe import views

urlpatterns = [
    path('ingredients/', views.IngredientListView.as_view(), name='ingredients'),
]
