from django.db import models

from account.models import BaseUser
from utils.regex_validators import crm_regex
# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField('account.BaseUser', on_delete=models.CASCADE, primary_key=True)
    contract_date = models.DateField('data do contrato')
    salary = models.DecimalField('salário',decimal_places=2, max_digits=12)

class Doctor(models.Model):
    employee = models.OneToOneField('employee.Employee', on_delete=models.CASCADE, primary_key=True)
    crm = models.CharField("crm (formato CRM/UF XXXXXX)", max_length=13, validators=[crm_regex], unique=True)
    specialty = models.CharField("especialidade", max_length=100)

    def __str__(self):
        doc_name = self.employee.user.name
        return f"Dr. {doc_name}. {self.crm}"