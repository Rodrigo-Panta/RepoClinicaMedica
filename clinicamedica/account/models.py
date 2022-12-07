from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.regex_validators import *

# Create your models here.
class BaseUser(AbstractUser):
    name = models.CharField('nome', max_length=200)
    email = models.EmailField('email', unique=True)
    phone = models.CharField('telefone', validators=[phone_regex], max_length=11)
    cep = models.CharField('cep', validators=[cep_regex], max_length=8)
    street_data = models.CharField('logradouro',max_length=200)
    neighborhood = models.CharField('bairro', max_length=200)
    city = models.CharField('cidade',max_length=100)
    state = models.CharField('estado', max_length=100)
