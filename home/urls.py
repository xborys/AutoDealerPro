from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('faq', views.FAQ, name='faq'),
    path('index', views.index, name='index'),
    path('car-list', views.car_list, name='car-list'),
    path('partner-list', views.partner_list, name='partner-list'),
    path('sale-transaction', views.sale_transaction, name='sale-transaction'),
    path('add-client', views.add_client, name='add-client'),
    path('clients-list', views.clients_list , name='clients-list'),
    path('show-client/<client_id>', views.show_client, name='show-client'),
    path('edit-client/<client_id>', views.edit_client, name='edit-client'),
    path('delete-client/<client_id>', views.delete_client, name='delete-client'),
    path('add-order', views.add_order, name='add-order'),
    path('edit-order/<order_id>', views.edit_order, name='edit-order'),
    path('delete-order/<order_id>', views.delete_order, name='delete-order'),
    path('show-order/<order_id>', views.show_order, name='show-order'),
    
    
]