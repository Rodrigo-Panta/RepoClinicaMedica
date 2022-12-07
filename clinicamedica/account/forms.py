from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

from .models import BaseUser

from utils.regex_validators import phone_regex, cep_regex

class BaseUserForm(forms.ModelForm):
    class Meta:
        model = BaseUser
        fields = ['name', 'email', 'phone', 'cep', 'street_data', 'neighborhood', 'city','state']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
