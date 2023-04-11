from django.shortcuts import render, redirect
from .models import Orders, Car, Clients
from .forms import ClientsForm, OrderForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required


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

@login_required
def clients_list(request):
    order_by = request.GET.get('order_by', 'name')
    clients = Clients.objects.all().order_by(order_by)

    if request.GET.get('search_name'):
        clients = clients.filter(name__icontains=request.GET.get('search_name'))

    if request.GET.get('search_pesel'):
        pesel = request.GET.get('search_pesel')
        if pesel:
            clients = clients.filter(pesel=pesel)

    if request.GET.get('search_nip'):
        nip = request.GET.get('search_nip')
        if nip:
            clients = clients.filter(nip=nip)

    context = {'clients': clients, 'order_by': order_by}
    return render(request, 'clients_list.html', context)

@login_required
def show_client(request, client_id):
    client = Clients.objects.get(pk=client_id)
   
    return render(request, 'Show_Client.html',
                  {'client': client})

@login_required
def edit_client(request, client_id):
    client = Clients.objects.get(pk=client_id)
    form = ClientsForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('clients-list')

    return render(request, 'edit_client.html', 
                  {'client': client,
                   'form': form})

@login_required
def delete_client(request, client_id):
    client = Clients.objects.get(pk=client_id)
    client.delete()
    return redirect('clients-list')

@login_required
def add_order(request):
    submitted = False
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-order?submitted=True')
    else:
        form = OrderForm
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'add_order.html',
                  {'form':form, 'submitted':submitted})

@login_required
def edit_order(request, order_id):
    order = Orders.objects.get(pk=order_id)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('sale-transaction')

    return render(request, 'edit_order.html', 
                  {'order': order,
                   'form': form})

@login_required
def delete_order(request, order_id):
    order = Orders.objects.get(pk=order_id)
    order.delete()
    return redirect('sale-transaction')

@login_required
def show_order(request, order_id):
    order = Orders.objects.get(pk=order_id)

    return render (request, 'show_order.html',
                   {'order': order})
