from django.urls import path
from . import views

app_name='employee'

urlpatterns = [
    path('create/', views.employee_create, name='create_employee'),
    path('list/', views.employee_create, name='list_employee'),
    path('api/get_doctors', views.get_doctors, name='api_get_doctors'),
    path('api/get_doctors/<specialty>', views.get_doctors, name='api_get_doctors'),

]