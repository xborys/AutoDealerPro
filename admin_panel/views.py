from django.shortcuts import render, redirect
from .models import *
from home.models import *
from django.http import HttpResponseRedirect
from django.db.models import Q, Sum, Count
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit



@login_required
def home(request):

    return render(request, 'home.html', {})

@login_required
def cars(request):
    car_list = Car.objects.all()
    current_time = timezone.now()
    for car in car_list:
        car.reserved = CarReservation.objects.filter(car=car, start_date__lte=current_time, end_date__gte=current_time).exists()
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

    # Get filter parameters from the request
    name_filter = request.GET.get('name', '')
    pesel_filter = request.GET.get('pesel', '')
    nip_filter = request.GET.get('nip', '')
    adress_filter = request.GET.get('adress', '')
    city_filter = request.GET.get('city', '')
    zip_filter = request.GET.get('zip', '')
    phone_filter = request.GET.get('phone', '')
    email_filter = request.GET.get('email', '')

    # Apply filters to the queryset
    if name_filter:
        clients_list = clients_list.filter(name__icontains=name_filter)
    if pesel_filter:
        clients_list = clients_list.filter(pesel__exact=pesel_filter)
    if nip_filter:
        clients_list = clients_list.filter(nip__exact=nip_filter)
    if adress_filter:
        clients_list = clients_list.filter(adress__icontains=adress_filter)
    if city_filter:
        clients_list = clients_list.filter(city__icontains=city_filter)
    if zip_filter:
        clients_list = clients_list.filter(zip__exact=zip_filter)
    if phone_filter:
        clients_list = clients_list.filter(phone__exact=phone_filter)
    if email_filter:
        clients_list = clients_list.filter(email__icontains=email_filter)

    return render(request, 'clients.html', {'clients' : clients_list})

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

from django.shortcuts import get_object_or_404, redirect
from .models import Contact, yes_no

@login_required
def mark_as_answered(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    yes_answer = get_object_or_404(yes_no, yes_no='Tak')
    contact.answer = yes_answer
    contact.save()
    return redirect('admin_panel:contact')  # zaktualizuj na odpowiednią nazwę dla Twojego projektu



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
def edit_transaction(request, transaction_id):
    submitted = False
    transaction = Transaction.objects.get(pk=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transakcja został edytowany.')
            return HttpResponseRedirect(reverse('admin_panel:transaction') + '?submitted=True')
    else:
        form = TransactionForm(instance=transaction)
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'edit_transaction.html', {'form': form, 'submitted': submitted})

@login_required
def del_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    transaction.delete()
    return redirect('admin_panel:transaction')

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

@login_required
def car_on_sale(request):
    car_on_sale = CarOnSale.objects.all()

    return render(request, 'car_on_sale.html',
                  {'car_on_sale' : car_on_sale})

@login_required
def add_car_on_sale(request):
    submitted = False
    
    if request.method == 'POST':
        form = CarSaleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Samochód został dodany.')
            return HttpResponseRedirect(reverse('admin_panel:cars-on-sale') + '?submitted=True')
    else:
        form = CarSaleForm
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'add_car_sale.html', {'form':form, 'submitted':submitted})

@login_required
def car_reservations(request):
    car_reservation = CarReservation.objects.all()

    return render(request, 'car_reservation.html',
                  {'car_reservation' : car_reservation})

@login_required
def add_car_reservation(request):
    submitted = False
    form_car = CarReservationForm(request.POST or None)
    form_client = ClientsForm(request.POST or None)

    if request.method == 'POST':
        if form_client.is_valid():
            form_client.save()
            messages.success(request, 'Klient został dodany.')
            form_client = ClientsForm()  # Clear the form
        if form_car.is_valid():
            form_car.save()
            messages.success(request, 'Rezerwacja została dodana.')
            return HttpResponseRedirect(reverse('admin_panel:car-reservations') + '?submitted=True')
        
    if 'submitted' in request.GET:
        submitted = True

    return render(request, 'add_car_reservation.html', {'form_car':form_car, 'form_client':form_client, 'submitted':submitted})

@login_required
def report_view(request):
    form = ReportForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        month = form.cleaned_data['month']
        year = form.cleaned_data['year']
        transactions = Transaction.objects.filter(date__year=year, date__month=month)

        # Zliczamy liczbę transakcji
        total_sales = transactions.count()

        context['transactions'] = transactions
        context['total_sales'] = total_sales

        # Sprawdzamy, czy istnieją jakiekolwiek transakcje
        if not transactions:
            context['no_sales'] = True

    return render(request, 'report.html', context)

@login_required
def contract_view(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    client = transaction.client
    car = transaction.car
    
    context = {
        'transaction': transaction,
        'client': client,
        'car': car,
    }

    # Renderujesz HTML jako string
    html_string = render_to_string('contract.html', context)

    # Generujesz PDF za pomocą pdfkit
    pdf = pdfkit.from_string(html_string, False)

    # Zapisujesz plik PDF na dysku
    with open('contract.pdf', 'wb') as f:
        f.write(pdf)

    # Otwierasz plik PDF i zwracasz go jako odpowiedź
    with open('contract.pdf', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=contract.pdf'
        return response
    
def sale_report_view(request):
    form = ReportForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        month = form.cleaned_data['month']
        year = form.cleaned_data['year']
        transactions = Transaction.objects.filter(date__year=year, date__month=month)
        total_sales = transactions.aggregate(Sum('price'))
        context['transactions'] = transactions
        context['total_sales'] = total_sales

        # Sprawdzamy, czy istnieją jakiekolwiek transakcje
        if not transactions:
            context['no_sales'] = True

    return render(request, 'salereport.html', context)





