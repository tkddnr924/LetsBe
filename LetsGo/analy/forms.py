from django import forms
from django.views.generic.edit import FormView

# --- form 설정

class PhotoForm(forms.Form):
    user = forms.CharField(max_length=50)
    image = forms.ImageField()

class SearchUserForm(forms.Form):
    search_word = forms.CharField(label="Search User")