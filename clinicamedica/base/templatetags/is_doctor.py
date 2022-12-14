from employee.models import Employee, Doctor
from django import template

register = template.Library()

def is_doctor(user):
    try:
        doctor = Doctor.objects.get(employee=Employee.objects.get(user=user))
        return True
    except:
        return False    

register.filter('is_doctor', is_doctor)
