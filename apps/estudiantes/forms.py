from django import forms
from .models import registrado

class regform(forms.Form):
     codigo = forms.IntegerField()
     nombre = forms.CharField(max_length=60)