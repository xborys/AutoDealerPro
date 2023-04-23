from django.db import models
from home.models import *

class Transaction(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='transactions', db_index=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='transactions', db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__ (self):
        return f"{self.client.name} | {self.car.make} {self.car.model}"