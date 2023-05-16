from django import forms
from django.forms import ModelForm
from .models import Clients, Orders, Contact, Car
from admin_panel.models import *
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

class ClientOpinionForm(ModelForm):
    class Meta:
        model = client_opinion
        fields = ('client_name', 'client_mail', 'client_score', 'client_opinion', 'rodo')

        labels = {
            'client_name' : '', 
            'client_mail' : '', 
            'client_score' : '', 
            'client_opinion' : '', 
            'rodo' : 'Zgoda RODO',
        }

        widgets = {
            'client_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Imię i nazwisko'}),
            'client_mail': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres email'}),
            'client_score': forms.Select(attrs={'class':'form-control', 'placeholder':'Ocena'}),
            'client_opinion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Opinia'}),
            'rodo': forms.CheckboxInput(attrs={'class':'form-check-input', 'label':'Akceptuję warunki RODO'}),
        }

class CarFilterForm(forms.Form):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'mileage', 'engine_capacity', 'engine_power', 'fuel_type', 'gear')

        labels = {
            'make': '',
            'model': '',
            'year': '',
            'mileage': '',
            'engine_capacity': '',
            'engine_power': '',
            'fuel_type': '',
            'gear': '',
        }

        widgets = {
            'make': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marka'}),
            'year': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Rok produkcji'}),
            'mileage': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Przebieg'}),
            'engine_capacity': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Pojemność silnika'}),
            'engine_power': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Moc silnika'}),
            'fuel_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rodzaj paliwa'}),
            'gear': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skrzynia biegów'}),
        }