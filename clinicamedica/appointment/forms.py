from django import forms

from .models import Appointment 

from employee.models import Doctor
from utils.regex_validators import *

class AppointmentForm(forms.ModelForm):

    specialty=forms.ChoiceField(choices=[(None, '-------------')]+[(sp,sp) for sp in list(Doctor.objects.values_list('specialty', flat=True).distinct())])
    date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )
    class Meta:
        model = Appointment
        fields="__all__"