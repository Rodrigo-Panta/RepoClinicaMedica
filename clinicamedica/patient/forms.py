
from django.contrib.auth import get_user_model
from django import forms

from account.forms import BaseUserForm

from .models import Patient 
from utils.regex_validators import *
from utils.blood_types import blood_types

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = ["weight", 'height', 'blood_type']