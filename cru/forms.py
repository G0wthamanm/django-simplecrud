from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserAddForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'abc@mail.com'}))
    class meta:
        models=User
        field=['username','email','password1','password2']

class UserLogin(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))