from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

from account.forms import BaseUserForm

from utils.regex_validators import *
from utils.blood_types import blood_types

class PatientCreateForm(BaseUserForm):
    weight = forms.DecimalField(label='Peso', max_digits=6, decimal_places=2)
    height = forms.DecimalField(label='Altura', max_digits=5, decimal_places=2)
    blood_type = forms.ChoiceField(label='Tipo Sanguíneo', choices=blood_types)