from django import forms
from django.forms import ModelForm
from .models import Clients

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
        

