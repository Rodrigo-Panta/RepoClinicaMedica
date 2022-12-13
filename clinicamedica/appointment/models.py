from django.db import models
from django.urls import reverse

from utils.regex_validators import phone_regex

# Create your models here.
class Appointment(models.Model):
    specialty = models.CharField("especialidade", max_length=100)
    doctor = models.ForeignKey('employee.Doctor', on_delete=models.CASCADE)
    date = models.DateField('data')
    time = models.CharField('hora', choices=[
        ('8', '8:00'),('9', '9:00'),('10', '10:00'),('11', '11:00'),('12', '12:00'),('13', '13:00'),('14', '14:00'),('15', '15:00'),('16', '16:00'),("17", '17:00')
    ], max_length=10)
    nome = models.CharField("nome", max_length=200)    
    email = models.EmailField()
    phone = models.CharField('telefone', validators=[phone_regex], max_length=11)

    def get_absolute_url(self):
        return reverse("index")
    