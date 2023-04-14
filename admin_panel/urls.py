from django.urls import path
from admin_panel import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.cars, name='cars'),
    path('clients/', views.clients, name='clients'),
    path('clients/add-client/', views.add_client, name='add-client'),
    path('clients/del-client/<client_id>', views.del_client , name='del-client'),
    path('contact/', views.contact, name='contact')
]