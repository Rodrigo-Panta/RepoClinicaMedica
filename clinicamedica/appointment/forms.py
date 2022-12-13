from django import forms

from .models import Appointment 

from employee.models import Doctor
from utils.regex_validators import *

class AppointmentForm(forms.ModelForm):

    specialty=forms.ChoiceField(choices=[(None, '-------------')]+[(sp,sp) for sp in list(Doctor.objects.values_list('specialty', flat=True).distinct())])
    doctor = forms.ChoiceField(choices=[(None, '-------------')])
    class Meta:
        model = Appointment
        fields="__all__"