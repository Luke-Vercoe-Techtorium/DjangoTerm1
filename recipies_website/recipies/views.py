from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from . import models

def home(request: HttpRequest) -> HttpResponse:
    return render(request, "recipies/home.html", {
        "title": "Home Page",
        "recipies": models.Recipie.objects.all,
    })

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "recipies/about.html", {
        "title": "About Page",
    })
