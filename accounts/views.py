from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class register(generic.CreateView):
    form_class = UserCreationForm
    model = User
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
