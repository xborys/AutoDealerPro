from django import forms
from django.forms import ModelForm
from home.models import *
from .models import *
from django.forms.widgets import NumberInput
from django.contrib.admin.widgets import AdminDateWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        fields = ('name', 'pesel', 'nip', 'adress', 'city', 'zip', 'phone', 'email')

        labels = {
            'name': '',
            'pesel': '',
            'nip': '',
            'adress': '',
            'city': '',
            'zip': '',
            'phone': '',
            'email': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Imię i nazwisko / Nazwa firmy'}),
            'pesel': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'PESEL'}),
            'nip': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'NIP'}),
            'adress': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Miasto'}),
            'zip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kod pocztowy'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numer telefonu'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres email'}),
        }

date = [2022, 2023, 2024]

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ('client', 'car', 'employee', 'order_date', 'order_price', 'order_status')

        labels ={
            'client': 'Kupujący',
            'car': 'Samochód',
            'employee': 'Sprzedawca',
            'order_date': 'Data ',
            'order_price': 'Data transakcji',
            'order_status': '',
        }

        widgets = {
            'client': forms.Select(attrs={'class':'form-control'}),
            'car': forms.Select(attrs={'class':'form-control'}),
            'employee': forms.Select(attrs={'class':'form-control'}),
            'order_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'order_price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Kwota transakcji'}),
            'order_status': forms.Select(attrs={'class':'form-control'}),
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

        labels = {
            'name': '',
            'email': '',
            'message': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Imię i nazwisko'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres email'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Wiadomość'}),
        }

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'vin', 'year', 'price', 'mileage', 'description', 'engine_capacity', 'engine_power', 'fuel_type', 'gear', 'type', 'color', 'seats', 'doors', 'availability', 'image')

        labels = {
            'make': 'Marka',
            'model': 'Model',
            'year': 'Rok produkcji',
            'mileage': 'Przebieg',
            'engine_capacity': 'Pojemność silnika',
            'engine_power': 'Moc silnika',
            'fuel_type': 'Rodzaj paliwa',
            'gear': 'Rodzaj skrzyni biegów',
            'type': 'Typ', 
            'color': 'Kolor', 
            'seats': 'Liczba miejsc', 
            'doors': 'Liczba drzwi',
            'vin': 'VIN',
            'price': 'Cena',
            'description': 'Opis',
            'availability': 'Czy wyświetlać na stronie?',
            'image': 'Zdjęcie',
        }

        widgets = {
            'make': forms.Select(attrs={'class':'form-control', 'placeholder':'Marka', 'required': True}),
            'model': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Model', 'required': True}),
            'year': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rok produkcji', 'required': True}),
            'mileage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Przebieg', 'required': True}),
            'engine_capacity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pojemność silnika', 'required': True}),
            'engine_power': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Moc silnika', 'required': True}),
            'fuel_type': forms.Select(attrs={'class':'form-control', 'placeholder':'Rodzaj paliwa', 'required': True}),
            'gear': forms.Select(attrs={'class':'form-control', 'placeholder':'Skrzynia biegów', 'required': True}),
            'type': forms.Select(attrs={'class':'form-control', 'placeholder':'Typ nadwozia', 'required': True}),
            'color': forms.Select(attrs={'class':'form-control', 'placeholder':'Kolor', 'required': True}),
            'seats': forms.Select(attrs={'class':'form-control', 'placeholder':'Liczba miejsc', 'required': True}),
            'doors': forms.Select(attrs={'class':'form-control', 'placeholder':'Liczba drzwi', 'required': True}),
            'vin': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numer VIN', 'required': True}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cena', 'required': True}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Opis', 'required': True}),
            'availability': forms.CheckboxInput(attrs={'placeholder':'Dostępność'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
        }

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ('client', 'car', 'price', 'is_paid')

        labels = {
            'client': '',
            'car': '',
            'price': '',
            'is_paid': '',
        }

        widgets = {
            'client': forms.Select(attrs={'class':'form-control'}),
            'car': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Kwota transakcji'}),
            'is_paid': forms.CheckboxInput(attrs={}),
        }

class CarSaleForm(ModelForm):
    class Meta:
        model = CarOnSale
        fields = ('car', 'new_price', 'start_date', 'end_date')

        labels = {
            'car': '',
            'new_price': '',
            'start_date': '',
            'end_date': '',
        }

        widgets = {
            'car': forms.Select(attrs={'class':'form-control'}),
            'new_price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Nowa cena'}),
            'start_date': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }