
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Employee, Doctor
from .forms import EmployeeForm

from account.models import BaseUser
from account.forms import BaseUserForm

from utils.error_messages import REGISTERED_USER_ERROR_MESSAGE
# Create your views here.

@login_required
def employee_create(request):
    if request.method == 'POST':
        user_form = BaseUserForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        
        if user_form.is_valid() and employee_form.is_valid():
            if len(BaseUser.objects.filter(email=user_form.cleaned_data['email'])): 
                user_form.add_error("email", REGISTERED_USER_ERROR_MESSAGE)
            else: 
                user = user_form.save(commit=False)
                user.username = user_form.cleaned_data['email']
                user.set_password(employee_form.cleaned_data['password'])

                employee = employee_form.save(commit=False)
                employee.user = user 

                user.save()
                employee.save()

                if(employee_form.cleaned_data['is_doctor']):
                    doctor = Doctor(
                        employee=employee,
                        crm = employee_form.cleaned_data['crm'],
                        specialty = employee_form.cleaned_data['specialty'],
                    )
                    doctor.save()

       
                return redirect('index') # TODO: Mudar para list view quando tiver pronta
        else:
            for error in user_form.errors:
                print(error)
            for error in employee_form.errors:
                print(error)
    else:
        user_form = BaseUserForm() 
        employee_form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'user_form':user_form, 'employee_form':employee_form})


def get_doctors(request, specialty):
    if specialty is None:
        return JsonResponse({'doctors':[f"{doctor}" for doctor in Doctor.objects.all()]})
    else:
        return JsonResponse({'doctors':[f"{doctor}" for doctor in Doctor.objects.filter(specialty=specialty)]})
