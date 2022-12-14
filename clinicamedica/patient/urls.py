from django.urls import path
from . import views

app_name='patient'

urlpatterns = [
    path('create/', views.patient_create, name='create_patient'),
    path('list/', views.PatientListView.as_view(), name='list_patient'),
]