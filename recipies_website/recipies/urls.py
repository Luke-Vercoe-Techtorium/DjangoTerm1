from django.urls import path
from . import views

urlpatterns = [
    path("", views.RecipieListView.as_view(), name="recipies-home"),
    path("recipe/<int:pk>", views.RecipieDetailView.as_view(), name="recipies-detail"),
    path("recipe/create", views.RecipieCreateView.as_view(), name="recipies-create"),
    path("recipe/<int:pk>/update", views.RecipieUpdateView.as_view(), name="recipies-update"),
    path("recipe/<int:pk>/delete", views.RecipieDeleteView.as_view(), name="recipies-delete"),
]
