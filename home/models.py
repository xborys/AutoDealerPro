from django.db import models

class Car(models.Model):
    make = models.CharField('Marka', max_length=50)
    model = models.CharField('Model', max_length=50)
    vin = models.CharField('VIN', max_length=17)
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
    
class Order_status(models.Model):
    status = models.CharField('Status', max_length=50)
    
    def __str__(self):
        return self.status

class Orders(models.Model):
    order_number = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_date = models.DateField('Data transakcji')
    order_price = models.IntegerField('Kwota transakcji')
    order_status = models.ForeignKey(Order_status, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.client.name + ' | ' + self.car.make + ' ' + self.car.model
 