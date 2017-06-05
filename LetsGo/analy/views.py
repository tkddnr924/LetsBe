from django.views.generic import ListView, DetailView
from django.shortcuts import render
from analy.models import Photo, User

# Create your views here.

class PhotoByUserLV(ListView):
    model = Photo


