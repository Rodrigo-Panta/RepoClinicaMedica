from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.regex_validators import *

# Create your models here.
class BaseUser(AbstractUser):
    email = models.EmailField('email', unique=True)
    phone = models.CharField('telefone', validators=[phone_regex], max_length=11)
    cep = models.CharField('cep', validators=[cep_regex], max_length=8)
    street_data = models.CharField('logradouro',max_length=200)
    neighborhood = models.CharField('bairro', max_length=200)
    city = models.CharField('city',max_length=100)
    
