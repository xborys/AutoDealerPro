from django.shortcuts import render
from .models import Orders, Car, Clients
from .forms import ClientsForm
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'index.html', {})

def FAQ(request):
    return render(request, 'FAQ.html', {})

def index(request):
    return render(request, 'index.html', {})

def CarList(request):
    car_list = Car.objects.all()
    return render(request, 'CarList.html', 
                  {'car_list': car_list})

def LP(request):
    return render(request, 'partnerzy.html', {})

def Sale_Transaction(request):
    order_list = Orders.objects.all()
    return render(request, 'Sale_Transaction.html', 
                  {'order_list': order_list})
    
def Add_Clients(request):
    submitted = False
    
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_client?submitted=True')
    else:
        form = ClientsForm
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'Add_Clients.html',
                  {'form':form, 'submitted':submitted})

def ClientsList(request):
    clients_list = Clients.objects.all()
    return render(request, 'ClientsList.html', 
                  {'clients_list': clients_list})