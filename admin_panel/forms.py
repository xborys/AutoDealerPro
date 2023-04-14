from django import forms
from django.forms import ModelForm
from home.models import *
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
        fields = ('make', 'model', 'vin', 'year', 'price', 'mileage', 'description', 'engine_capacity', 'engine_power', 'fuel_type', 'gear', 'image')

        labels = {
            'make': '',
            'model': '',
            'year': '',
            'mileage': '',
            'engine_capacity': '',
            'engine_power': '',
            'fuel_type': '',
            'gear': '',
            'vin': '',
            'price': '',
            'description': '',
            'image': '',
        }

        widgets = {
            'make': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marka'}),
            'model': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Model'}),
            'year': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Rok produkcji'}),
            'mileage': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Przebieg'}),
            'engine_capacity': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Pojemność silnika'}),
            'engine_power': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Moc silnika'}),
            'fuel_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rodzaj paliwa'}),
            'gear': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skrzynia biegów'}),
            'vin': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numer VIN'}),
            'price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cena'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Opis'}),
            'image': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Zdjęcie'}),
        }