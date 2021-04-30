from django import forms
# from django.forms import Modelform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserCheck


class CheckForm(forms.ModelForm):
    class Meta:
        model=UserCheck
        fields=('ispermit',)
