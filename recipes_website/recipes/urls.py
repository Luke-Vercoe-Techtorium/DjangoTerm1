from django.urls import path
from . import views

urlpatterns = [
    path("", views.recipeListView.as_view(), name="recipes-home"),
    path("health_diet", views.recipeHealthDietView.as_view(), name="recipes-health-diet"),
    path("holidays", views.recipeHolidaysView.as_view(), name="recipes-holidays"),
    path("breakfast", views.recipeBreakfastView.as_view(), name="recipes-breakfast"),
    path("lunch", views.recipeLunchView.as_view(), name="recipes-lunch"),
    path("dinner", views.recipeDinnerView.as_view(), name="recipes-dinner"),
    path("dessert", views.recipeDessertView.as_view(), name="recipes-dessert"),
    path("recipe/<int:pk>", views.recipeDetailView.as_view(), name="recipes-detail"),
    path("recipe/create", views.recipeCreateView.as_view(), name="recipes-create"),
    path("recipe/<int:pk>/update", views.recipeUpdateView.as_view(), name="recipes-update"),
    path("recipe/<int:pk>/delete", views.recipeDeleteView.as_view(), name="recipes-delete"),
]
