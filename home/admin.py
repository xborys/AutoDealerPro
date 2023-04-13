from django.contrib import admin
from .models import Car
from .models import Clients
from .models import Employee
from .models import Orders
from .models import Order_status
from .models import Contact

admin.site.register(Car)
admin.site.register(Clients)
admin.site.register(Employee)
admin.site.register(Orders)
admin.site.register(Order_status)
admin.site.register(Contact)
