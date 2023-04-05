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

def car_list(request):
    car_list = Car.objects.all()
    return render(request, 'Car_List.html', 
                  {'car_list': car_list})

def partner_list(request):
    return render(request, 'partner_list.html', {})

def sale_transaction(request):
    order_list = Orders.objects.all()
    return render(request, 'Sale_Transaction.html', 
                  {'order_list': order_list})
    
def add_client(request):
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

def clients_list(request):
    clients_list = Clients.objects.all()
    return render(request, 'Clients_List.html', 
                  {'clients_list': clients_list})

def show_client(request, client_id):
    client = Clients.objects.get(pk=client_id)
   
    return render(request, 'Show_Client.html',
                  {'client': client})