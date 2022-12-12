from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import Address

# Create your views here.
class AddressCreateView(CreateView):
    model = Address
    template_name = 'address/address_form.html'    
    fields = '__all__'


@login_required
def get_address(request, cep):
    if(cep == None):
        return JsonResponse({})
    address = Address.objects.filter(cep=cep)
    if(len(address)):   
        response = {
            'cep': address[0].cep,
            'street_data': address[0].street_data,
            'neighborhood': address[0].neighborhood,
            'city': address[0].city,
            'state': address[0].state,
        }
        return JsonResponse(response, safe=False)
    return JsonResponse({})