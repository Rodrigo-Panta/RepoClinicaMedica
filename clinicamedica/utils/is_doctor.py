from employee.models import *

def is_doctor(user):
    doctor = Doctor.objects.filter(employee=Employee.objects.filter(user=user))
    if(len(doctor)):
        return True
    else:
        return False    