from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField()
    category = models.CharField(max_length=100, choices=(
        ("NONE", "None"),
        ("HEALTH_DIET", "Health & Diet"),
        ("HOLIDAYS", "Holidays"),
    ))
    meal_time = models.CharField(max_length=100, choices=(
        ("BREAKFAST", "Breakfast"),
        ("LUNCH", "Lunch"),
        ("DINNER", "Dinner"),
        ("DESSERT", "Dessert"),
    ))

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={ "pk": self.pk })

    def __str__(self):
        return self.title
