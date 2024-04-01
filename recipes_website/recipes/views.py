from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models

class recipeListView(ListView):
    model = models.recipe
    template_name ="recipes/home.html"
    context_object_name = "recipes"

class recipeHealthDietView(ListView):
    model = models.recipe
    template_name ="recipes/health_diet.html"
    context_object_name = "recipes"

class recipeHolidaysView(ListView):
    model = models.recipe
    template_name ="recipes/holidays.html"
    context_object_name = "recipes"

class recipeBreakfastView(ListView):
    model = models.recipe
    template_name ="recipes/breakfast.html"
    context_object_name = "recipes"

class recipeLunchView(ListView):
    model = models.recipe
    template_name ="recipes/lunch.html"
    context_object_name = "recipes"

class recipeDinnerView(ListView):
    model = models.recipe
    template_name ="recipes/dinner.html"
    context_object_name = "recipes"

class recipeDetailView(DetailView):
    model = models.recipe

class recipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.recipe
    success_url = reverse_lazy("recipes-home")

    def test_func(self):
        recipe = self.get_object()
        return self.request.user.is_staff or self.request.user == recipe.author

class recipeCreateView(LoginRequiredMixin, CreateView):
    model = models.recipe
    fields = ['title', 'description', 'category', 'meal_time']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class recipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.recipe
    fields = ['title', 'description', 'category', 'meal_time']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user.is_staff or self.request.user == recipe.author
