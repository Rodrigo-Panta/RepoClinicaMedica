from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

from utils.regex_validators import phone_regex, cep_regex

class BaseUserForm(forms.Form):
    first_name = forms.CharField(label='Nome', max_length=100, required=True)
    last_name = forms.CharField(label='Sobrenome', max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = forms.CharField(label='Telefone', validators=[phone_regex], max_length=11)
    cep = forms.CharField(label='CEP', validators=[cep_regex], max_length=8)
    street_data = forms.CharField(label='Logradouro', max_length=200)
    neighborhood = forms.CharField(label='Bairro', max_length=200)
    city = forms.CharField(label='Cidade', max_length=100)
    

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
