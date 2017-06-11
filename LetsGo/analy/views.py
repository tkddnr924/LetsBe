from django.views.generic import ListView, DetailView
from django.shortcuts import render
from analy.models import Photo, User

# Create your views here.

class UserDV(DetailView):
    model = User
    template_name = 'analy/analy_result.html'


class UserLV(ListView):
    model = User
    template_name = 'analy/analy_other_user.html'



# GET JSON 필요
