from django.shortcuts import render, redirect
from .models import *
from home.models import *
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.urls import reverse

@login_required
def home(request):

    return render(request, 'home.html', 
                  {})

@login_required
def cars(request):
    car_list = Car.objects.all()
    return render(request, 'cars.html', 
                  {'car_list': car_list})

@login_required
def clients(request):
    clients_list = Clients.objects.all()

    return render(request, 'clients.html',
                  {'clients' : clients_list})

@login_required
def add_client(request):
    submitted = False
    
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Klient został dodany.')
            return HttpResponseRedirect(reverse('admin_panel:clients') + '?submitted=True')
    else:
        form = ClientsForm
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'Add_Client.html', {'form':form, 'submitted':submitted})

@login_required
def del_client(request, client_id):
    client = Clients.objects.get(pk=client_id)
    client.delete()
    messages.error(request, 'Klient ' + str(client) +' został usunięty.')
    return redirect('admin_panel:clients')