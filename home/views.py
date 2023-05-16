from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import CarFilter
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def home(request):
    submitted = False
    opinion = client_opinion.objects.all()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect('/index?submitted=True')
    else:
        contact_form = ContactForm
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'index.html',
                  {'contact_form': contact_form, 'submitted': submitted, 'opinion': opinion})

def FAQ(request):
    return render(request, 'FAQ.html', {})

def index(request):
    submitted = False

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect('/index?submitted=True')
    else:
        contact_form = ContactForm
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'index.html',
                  {'contact_form': contact_form, 'submitted': submitted})

def car_list(request):
    car_list = Car.objects.all()

    # Filtering
    car_filter = CarFilter(request.GET, queryset=car_list)
    car_list = car_filter.qs

    # Sorting
    sort_by = request.GET.get('sort_by')

    if sort_by in ['make', 'model', 'price', 'year']:
        car_list = car_list.order_by(sort_by)
    
    return render(request, 'Car_List.html', 
                  {'car_list': car_list, 'filter': car_filter})



def car_details(request, car_id):
    car = Car.objects.get(pk=car_id)
    return render(request, 'Car_Details.html', 
                  {'car': car})

def partner_list(request):
    return render(request, 'partner_list.html', {})

def add_opinion(request):
    submitted = False
    
    if request.method == 'POST':
        form = ClientOpinionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index') + '?submitted=True')
    else:
        form = ClientOpinionForm
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'add_opinion.html',
                  {'form': form, 'submitted': submitted})

def financing(request):
    return render(request, 'financing.html', {})
