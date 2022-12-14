from django.urls import path
from . import views

app_name='appointment'

urlpatterns = [
    path('create/', views.AppointmentCreateView.as_view(), name='create_appointment'),
    path('list/', views.AppointmentListView.as_view(), name='list_appointment'),
    path('list/doc', views.doctor_appointments, name='doctor_appointments'),
    path('api/get_available_times', views.api_get_available_times, name='api_get_available_times'),
    path('api/get_available_times/<doctor_id>/<date>', views.api_get_available_times, name='api_get_available_times'),
]
