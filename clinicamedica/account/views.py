from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from .models import BaseUser

from employee.models import Employee
from utils.error_messages import EMPLOYEE_NOT_FOUND_ERROR_MESSAGE

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            try:
                employee = Employee.objects.get(user = BaseUser.objects.get(email=email))
                password = request.POST['password'] 
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('index')
            except:
                pass
        form.errors['__all__']= form.error_class([EMPLOYEE_NOT_FOUND_ERROR_MESSAGE])

    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')