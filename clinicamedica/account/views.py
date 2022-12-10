from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

from patient.models import Patient
from utils.error_messages import PATIENT_EMAIL_ERROR_MESSAGE

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            email = request.POST['username']
            if(len(Patient.objects.filter(email=email))):
                form.add_error('email', PATIENT_EMAIL_ERROR_MESSAGE)
            else:
                password = request.POST['password']
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('index')
    else:
        form = LoginForm
    return render(request, 'account/login.html', {'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')