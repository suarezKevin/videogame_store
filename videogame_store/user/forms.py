from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account

class SigninForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2',]
        
class LoginForm(AuthenticationForm):
    pass
