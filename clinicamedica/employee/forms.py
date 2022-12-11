
from django.contrib.auth import get_user_model
from django import forms

from account.forms import BaseUserForm

from .models import Employee 
from utils.regex_validators import *
from utils.blood_types import blood_types

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(label="Senha", widget=forms.PasswordInput())
    is_doctor = forms.BooleanField(label='O funcionário é um médico?', required=False)
    crm = forms.CharField(label="crm (formato CRM/UF XXXXXX)", max_length=13, validators=[crm_regex], required=False)
    specialty = forms.CharField(label="especialidade", max_length=100, required=False)

    class Meta:
        model = Employee
        fields=['contract_date', 'salary']