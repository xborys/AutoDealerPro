from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class CarFuelType(models.Model):
    fuel_type = models.CharField('Rodzaj paliwa', max_length=50)

    def __str__(self):
        return self.fuel_type
    
class CarGear(models.Model):
    gear = models.CharField('Skrzynia biegów', max_length=50)

    def __str__(self):
        return self.gear
    
class vehicle_make(models.Model):
    make = models.CharField('Marka', max_length=50)

    def __str__(self):
        return self.make\
        
class yes_no(models.Model):
    yes_no = models.CharField('Wartość', max_length=3)

    def __str__(self):
        return self.yes_no



class Car(models.Model):
    car_make = [
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Ford', 'Ford'),
        ('Honda', 'Honda'),
        ('Hyundai', 'Hyundai'),
        ('Kia', 'Kia'),
        ('Mazda', 'Mazda'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Nissan', 'Nissan'),
        ('Opel', 'Opel'),
        ('Renault', 'Renault'),
        ('Skoda', 'Skoda'),
        ('Toyota', 'Toyota'),
        ('Tesla', 'Tesla'),
        ('Volkswagen', 'Volkswagen'),
    ]

    fuel_type = [
        ('benzyna', 'Benzyna'),
        ('diesel', 'Diesel'),
        ('hybryda', 'Hybryda'),
        ('elektryczny', 'Elektryczny'),
        ('lpg', 'LPG'),
    ]

    gear_type = [
        ('Manualna', 'Manualna'),
        ('Automatyczna', 'Automatyczna'),
    ]

    type = [
        ('Używane', 'Używane'),
        ('Nowe', 'Nowe'),
    ]

    color = [
        ('Biały', 'Biały'),
        ('Szary', 'Szary'),
        ('Czarny', 'Czarny'),
        ('Srebrny', 'Srebrny'),
        ('Niebieski', 'Niebieski'),
        ('Czerwony', 'Czerwony'),
        ('Zielony', 'Zielony'),
        ('Żółty', 'Żółty'),
        ('Brązowy', 'Brązowy'),
        ('Inny', 'Inny')
    ]

    seats = [
        ('2', '2'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7 lub wiecej', '7 lub wiecej'),
    ]

    doors = [
        ('2/3', '2/3'),
        ('4/5', '4/5'),
    ]

    make = models.CharField('Marka', max_length=50, choices=car_make)
    model = models.CharField('Model', max_length=50)
    vin = models.CharField('VIN', max_length=17)
    year = models.IntegerField('Rok produkcji')
    price = models.IntegerField('Cena (PLN)')
    mileage = models.IntegerField('Przebieg (km)')
    description = models.TextField('Opis')
    engine_capacity = models.IntegerField('Pojemność silnika (cm3)')
    engine_power = models.IntegerField('Moc silnika (KM)')
    fuel_type = models.CharField('Rodzaj paliwa', max_length=50, choices=fuel_type)
    gear = models.CharField('Skrzynia biegów', max_length=50, choices=gear_type)
    type = models.CharField('Typ', max_length=50, choices=type)
    color = models.CharField('Kolor', max_length=50, choices=color)
    seats = models.CharField('Liczba miejsc', max_length=50, choices=seats)
    doors = models.CharField('Liczba drzwi', max_length=50, choices=doors)
    availability = models.BooleanField('Dostępność', default=False)
    image = models.ImageField('Zdjęcia', upload_to='images/',blank=True, null=True)

    def __str__(self):
        return str(self.make) + ' ' + self.model
    
    
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
 
class Contact(models.Model):
    name = models.CharField('Imię i nazwisko', max_length=50)
    email = models.EmailField('Email')
    message = models.TextField('Wiadomość')
    answer = models.ForeignKey(yes_no, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

class client_opinion(models.Model):
    SCORE_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    client_name = models.CharField(max_length=100)
    client_mail = models.EmailField(max_length=100)
    client_score = models.CharField(choices=SCORE_CHOICES, max_length=1)
    client_opinion = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rodo = models.BooleanField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.client_name