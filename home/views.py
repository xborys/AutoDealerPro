from django.shortcuts import render
from .models import Orders

def home(request):
    return render(request, 'index.html', {})

def FAQ(request):
    return render(request, 'FAQ.html', {})

def index(request):
    return render(request, 'index.html', {})

def CarList(request):
    return render(request, 'CarList.html', {})

def LP(request):
    return render(request, 'partnerzy.html', {})

def Transakcje(request):
    order_list = Orders.objects.all()

    return render(request, 'transakcje.html', 
                  {'order_list': order_list})
