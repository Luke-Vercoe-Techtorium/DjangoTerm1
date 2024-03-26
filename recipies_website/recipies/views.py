from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from . import models

class RecipieListView(ListView):
    model = models.Recipie
    template_name ="recipies/home.html"
    context_object_name = "recipies"

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "recipies/about.html", {
        "title": "About Page",
    })
