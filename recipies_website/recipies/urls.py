from django.urls import path
from . import views

urlpatterns = [
    path("", views.RecipieListView.as_view(), name="recipies-home"),
]
