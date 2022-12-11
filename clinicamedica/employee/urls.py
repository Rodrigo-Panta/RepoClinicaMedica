from django.urls import path
from . import views

app_name='employee'

urlpatterns = [
    path('create/', views.employee_create, name='create'),
]