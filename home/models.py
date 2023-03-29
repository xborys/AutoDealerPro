from django.db import models

class Car(models.Model):
    make = models.CharField('Marka', max_length=50)
    model = models.CharField('Model', max_length=50)
    year = models.IntegerField('Rok produkcji')
    price = models.IntegerField('Cena (PLN)')
    mileage = models.IntegerField('Przebieg (km)')
    description = models.TextField('Opis')
    image = models.ImageField('Zdjęcia', upload_to='images/',blank=True, null=True)

    def __str__(self):
        return self.make + ' ' + self.model
    
class Clients(models.Model):
    name = models.CharField('Imię i nazwisko / Nazwa firmy', max_length=50)
    pesel = models.IntegerField('PESEL', blank=True, null=True)
    nip = models.IntegerField('NIP', blank=True, null=True)
    adress = models.CharField('Adres', max_length=100)
    city = models.CharField('Miasto', max_length=50)
    zip = models.IntegerField('Kod pocztowy')
    phone = models.IntegerField('Telefon')
    email = models.EmailField('Email')
    

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField('Imię i nazwisko', max_length=50)
    adress = models.CharField('Adres', max_length=100)
    city = models.CharField('Miasto', max_length=50)
    zip = models.IntegerField('Kod pocztowy')
    phone = models.IntegerField('Telefon')
    email = models.EmailField('Email')
    position = models.CharField('Stanowisko', max_length=50)
    hire_date = models.DateField('Data zatrudnienia')
    fire_date = models.DateField('Data zwolnienia', blank=True, null=True)
    
    def __str__(self):
        return self.name
 