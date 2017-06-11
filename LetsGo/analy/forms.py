from django import forms
from analy.fields import MyImageField

# --- form 설정

class PhotoForm(forms.Form):
    user = forms.CharField(max_length=50)
    image = forms.ImageField()

