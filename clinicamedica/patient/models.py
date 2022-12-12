from django.db import models
from utils.blood_types import blood_types
# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField('account.BaseUser', on_delete=models.CASCADE, primary_key=True)
    weight = models.DecimalField('peso', max_digits=6, decimal_places=2)
    height = models.DecimalField('altura', max_digits=5, decimal_places=2)
    blood_type = models.CharField('tipo sanguíneo', choices=blood_types, max_length=10)    
    