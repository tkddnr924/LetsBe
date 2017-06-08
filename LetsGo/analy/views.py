from django.views.generic import ListView, DetailView
from django.shortcuts import render
from analy.models import Photo, User

# Create your views here.

class UserDV(DetailView):
    model = User

class UserLV(ListView):
    model = User

# GET JSON 필요
