from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from .models import *

class EditUserForm(ModelForm):
    class Meta:
        model = Setting
        fields = '__all__'
        exclude = ['user_id'] 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2'] 


        