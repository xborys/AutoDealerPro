from django.shortcuts import render, redirect
from .models import *
from home.models import *
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404

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
def add_car(request):
    submitted = False
    
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Samochód został dodany.')
            return HttpResponseRedirect(reverse('admin_panel:cars') + '?submitted=True')
    else:
        form = CarForm
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'Add_Car.html', {'form':form, 'submitted':submitted})

@login_required
def show_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    
    return render(request, 'show_car.html', {'car': car})

@login_required
def del_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return redirect('admin_panel:cars')

@login_required
def edit_car(request, car_id):
    submitted = False
    car = Car.objects.get(pk=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, 'Samochód został edytowany.')
            return HttpResponseRedirect(reverse('admin_panel:cars') + '?submitted=True')
    else:
        form = CarForm(instance=car)
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'Edit_Car.html', {'form':form, 'submitted':submitted})

@login_required
def clients(request):
    clients_list = Clients.objects.all()

    return render(request, 'clients.html',
                  {'clients' : clients_list})

@login_required
def show_client(request, client_id):
    client = get_object_or_404(Clients, pk=client_id)
    transactions = Transaction.objects.filter(client_id=client.id)
    has_transactions = True if transactions.exists() else False
    
    context = {
        'client': client,
        'transactions': transactions,
        'has_transactions': has_transactions,
    }
    
    return render(request, 'show_client.html', context)

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
def edit_client(request, client_id):
    submitted = False
    client = Clients.objects.get(pk=client_id)
    if request.method == 'POST':
        form = ClientsForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Klient został edytowany.')
            return HttpResponseRedirect(reverse('admin_panel:clients') + '?submitted=True')
    else:
        form = ClientsForm(instance=client)
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'Edit_Client.html', {'form':form, 'submitted':submitted})

@login_required
def del_client(request, client_id):
    client = get_object_or_404(Clients, id=client_id)
    client.delete()
    return redirect('admin_panel:clients')

@login_required
def contact(request):
    contact = Contact.objects.all()

    return render(request, 'contact.html',
                    {'contact' : contact})

@login_required
def opinions(request):
    opinion = client_opinion.objects.all()

    return render(request, 'opinions.html',
                    {'opinion' : opinion})

@login_required
def del_opinion(request, opinion_id):
    opinion = get_object_or_404(client_opinion, id=opinion_id)
    opinion.delete()
    return redirect('admin_panel:opinions')


@login_required
def transaction(request):
    transaction = Transaction.objects.all()

    return render(request, 'transaction.html',
                  {'transaction' : transaction})

@login_required
def show_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    client = transaction.client
    car = transaction.car
    
    context = {
        'transaction': transaction,
        'client': client,
        'car': car,
    }

    return render(request, 'show_transaction.html', context)


@login_required
def add_transaction(request):
    submitted = False
    
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transakcja została dodana.')
            return HttpResponseRedirect(reverse('admin_panel:transaction') + '?submitted=True')
    else:
        form = TransactionForm
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'add_transaction.html', {'form':form, 'submitted':submitted})