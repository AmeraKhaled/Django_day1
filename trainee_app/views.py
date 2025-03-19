from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Trainee

class TraineeListView(LoginRequiredMixin, ListView):
    model = Trainee
    template_name = "trainee/trainee_list.html"
    context_object_name = "trainees"

# class TraineeDetailView(LoginRequiredMixin, DetailView):
#     model = Trainee
#     template_name = "trainee/trainee_detail.html"
#     context_object_name = "trainee"

class TraineeDeleteView(LoginRequiredMixin, DeleteView):
    model = Trainee
    template_name = "trainee/delete_trainee.html"
    success_url = reverse_lazy("traineelist")

class TraineeCreateView(LoginRequiredMixin, CreateView):
    model = Trainee
    fields = ["name", "email", "phone", "course"]
    template_name = "trainee/trainee_form.html"
    success_url = reverse_lazy("traineelist")

class TraineeUpdateView(LoginRequiredMixin, UpdateView):
    model = Trainee
    fields = ["name", "email", "phone", "course"]
    template_name = "trainee/trainee_form.html"
    success_url = reverse_lazy("traineelist")
