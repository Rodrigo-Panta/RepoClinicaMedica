from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Appointment
from .forms import AppointmentForm

from employee.models import Doctor, Employee
from django.contrib.auth.decorators import login_required
from account.models import BaseUser

from utils.time_choices import time_choices
# Create your views here.


class AppointmentCreateView(CreateView):
    model = Appointment
    template_name = 'appointment/appointment_form.html'    
    fields = '__all__'
    
class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointment/appointment_list.html'    
    fields = '__all__'    

@login_required
def doctor_appointments(request):
    user = request.user
    try:
        employee = Employee.objects.get(user=user)
        doctor = Doctor.objects.get(employee=employee)
        appointments = Appointment.objects.filter(doctor=doctor)
        return render(request, 'appointment/doctor_appointment.html', {'object_list':appointments, 'doctor':doctor})
    except:
        redirect('index')
    

def api_get_available_times(request, doctor_id, date):
    date_list = date.split('_')
    date = f'{date_list[2]}-{date_list[1]}-{date_list[0]}'
    unavailable_times = list(Appointment.objects.filter(date=date, doctor = Doctor.objects.get(employee = Employee.objects.get(user=BaseUser.objects.get(email=doctor_id)))).values_list('time', flat=True))
    available_times = []
    for it in time_choices:
        print(it)
        if not it in unavailable_times:
            available_times.append(it)
    return JsonResponse({'times':available_times})
    