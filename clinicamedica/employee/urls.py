from django.urls import path
from . import views

app_name='employee'

urlpatterns = [
    path('create/', views.employee_create, name='create_employee'),
    path('api/get_specialties', views.get_specialties, name='api_get_specialties'),

]