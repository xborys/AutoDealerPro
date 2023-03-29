from django.contrib import admin
from .models import Car
from .models import Clients
from .models import Employee

admin.site.register(Car)
admin.site.register(Clients)
admin.site.register(Employee)
