from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Patient
from .forms import PatientCreateForm

from account.models import BaseUser

# Create your views here.

@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientCreateForm(request.POST)
        if form.is_valid():
            
            if len(BaseUser.objects.filter(email=form.cleaned_data['email'])): 
                form.add_error("email", "Um usuário já foi cadastrado com esse email")
            else: 
                user = BaseUser.objects.create(
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    email = form.cleaned_data['email'],
                    username =form.cleaned_data['email'],
                        phone = form.cleaned_data['phone'],
                    cep = form.cleaned_data['cep'],
                    street_data = form.cleaned_data['street_data'],
                    neighborhood = form.cleaned_data['neighborhood'],
                    city = form.cleaned_data['city'],
                )
                patient = Patient.objects.create(
                    id = user,
                    weight=form.cleaned_data['weight'],
                    height=form.cleaned_data['height'],
                    blood_type=form.cleaned_data['blood_type']
                )
                return redirect('index') # TODO: Mudar para list view quando tiver pronta
        return render(request, 'patient/patient_create.html', {'form':form})
    else:
        form = PatientCreateForm() 
        return render(request, 'patient/patient_create.html', {'form':form})