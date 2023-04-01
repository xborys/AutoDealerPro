from django.shortcuts import render
from .models import Orders, Car, Clients

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

def Transakcje(request):
    order_list = Orders.objects.all()
    return render(request, 'transakcje.html', 
                  {'order_list': order_list})
    
def Add_Clients(request):
    return render(request, 'Clients.html', {})

def ClientsList(request):
    clients_list = Clients.objects.all()
    return render(request, 'ClientsList.html', 
                  {'clients_list': clients_list})