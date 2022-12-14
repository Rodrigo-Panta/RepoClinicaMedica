from django.db import models
from django.urls import reverse
from utils.time_choices import TIME_CHOICES 

from utils.regex_validators import phone_regex

# Create your models here.
class Appointment(models.Model):
    specialty = models.CharField("especialidade", max_length=100)
    doctor = models.ForeignKey('employee.Doctor', verbose_name="Médico", on_delete=models.CASCADE)
    date = models.DateField('data')
    time = models.CharField('hora', choices=TIME_CHOICES, max_length=10)
    nome = models.CharField("nome", max_length=200)    
    email = models.EmailField()
    phone = models.CharField('telefone', validators=[phone_regex], max_length=11)

    def get_absolute_url(self):
        return reverse("index")
    
    