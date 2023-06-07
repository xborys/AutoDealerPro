from django.db import models
from home.models import *

class DEALER(models.Model):
    name = models.CharField(max_length=250)
    nip = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=250)
    bank = models.CharField(max_length=250)
    bank_account = models.CharField(max_length=250)

    def __str__ (self):
        return self.name

class Transaction(models.Model):
    dealer = DEALER.objects.first()
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='transactions', db_index=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='transactions', db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__ (self):
        return f"{self.client.name} | {self.car.make} {self.car.model}"
    
class CarReservation(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='reservations', db_index=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reservations', db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__ (self):
        return f"{self.client.name} | {self.car.make} {self.car.model}"