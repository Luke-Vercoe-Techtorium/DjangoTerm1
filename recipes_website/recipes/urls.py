from django.urls import path
from . import views

urlpatterns = [
    path("", views.recipeListView.as_view(), name="recipes-home"),
    path("recipe/<int:pk>", views.recipeDetailView.as_view(), name="recipes-detail"),
    path("recipe/create", views.recipeCreateView.as_view(), name="recipes-create"),
    path("recipe/<int:pk>/update", views.recipeUpdateView.as_view(), name="recipes-update"),
    path("recipe/<int:pk>/delete", views.recipeDeleteView.as_view(), name="recipes-delete"),
]
