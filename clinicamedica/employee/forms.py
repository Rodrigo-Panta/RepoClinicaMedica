
from django.contrib.auth import get_user_model
from django import forms

from account.forms import BaseUserForm

from .models import Employee 
from utils.regex_validators import *

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(label="Senha", widget=forms.PasswordInput())
    is_doctor = forms.BooleanField(label='O funcionário é um médico?', required=False)
    crm = forms.CharField(label="CRM (formato CRM/UF XXXXXX)", max_length=13, validators=[crm_regex], required=False)
    specialty = forms.CharField(label="Especialidade", max_length=100, required=False)

    class Meta:
        model = Employee
        fields=['contract_date', 'salary']