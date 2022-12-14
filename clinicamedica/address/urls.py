from django.urls import path
from . import views

app_name='address'

urlpatterns = [
    path('create/', views.AddressCreateView.as_view(), name='create_address'),
    path('', views.AddressListView.as_view(), name='list_address'),
    path('list/', views.AddressListView.as_view(), name='list_address'),
    path('api/get/<cep>', views.get_address, name='api_get_address'),
    path('api/get', views.get_address, name='api_get_address'),
]