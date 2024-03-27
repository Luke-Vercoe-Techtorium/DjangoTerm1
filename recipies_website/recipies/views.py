from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models

class RecipieListView(ListView):
    model = models.Recipie
    template_name ="recipies/home.html"
    context_object_name = "recipies"

class RecipieDetailView(DetailView):
    model = models.Recipie

class RecipieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipie
    success_url = reverse_lazy("recipies-home")

    def test_func(self):
        recipie = self.get_object()
        return self.request.user.is_staff or self.request.user == recipie.author

class RecipieCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipie
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipie
    fields = ['title', 'description']

    def test_func(self):
        recipie = self.get_object()
        return self.request.user.is_staff or self.request.user == recipie.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
