from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Patient
from .forms import PatientForm

from account.models import BaseUser
from account.forms import BaseUserForm

# Create your views here.

@login_required
def patient_create(request):
    if request.method == 'POST':
        user_form = BaseUserForm(request.POST)
        patient_form = PatientForm(request.POST)
        
        if user_form.is_valid() and patient_form.is_valid():
            if len(BaseUser.objects.filter(email=user_form.cleaned_data['email'])): 
                user_form.add_error("email", "Um usuário já foi cadastrado com esse email")
            else: 
                user = user_form.save(commit=False)
                user.username = user_form.cleaned_data['email']

                patient = patient_form.save(commit=False)
                patient.user = user 
                
                user.save()
                patient.save()       
                
                return redirect('index') # TODO: Mudar para list view quando tiver pronta
    else:
        user_form = BaseUserForm() 
        patient_form = PatientForm()
    return render(request, 'patient/patient_create.html', {'user_form':user_form, 'patient_form':patient_form})