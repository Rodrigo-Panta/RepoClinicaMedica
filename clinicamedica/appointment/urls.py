from django.urls import path
from . import views

app_name='appointment'

urlpatterns = [
    path('create/', views.AppointmentCreateView.as_view(), name='create_appointment'),
]