from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Appointment

# Create your views here.


class AppointmentCreateView(CreateView):
    model = Appointment
    template_name = 'appointment/appointment_form.html'    
    fields = '__all__'

