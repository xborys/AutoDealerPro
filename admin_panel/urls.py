from django.urls import path
from admin_panel import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.cars, name='cars'),
    path('cars/show-car/<int:car_id>/', views.show_car, name='show-car'),
    path('cars/add-car/', views.add_car, name='add-car'),
    path('cars/del-car/<int:car_id>/', views.del_car, name='del-car'),
    path('cars/edit-car/<car_id>', views.edit_car, name='edit-car'),
    path('cars/cars-on-sale/', views.car_on_sale, name='cars-on-sale'),
    path('cars/cars-on-sale/add-car-on-sale', views.add_car_on_sale, name='add-car-on-sale'),
    path('cars/car-reservations', views.car_reservations, name='car-reservations'),
    path('cars/car-reservations/add-car-reservation', views.add_car_reservation, name='add-car-reservation'),
    path('clients/', views.clients, name='clients'),
    path('clients/add-client/', views.add_client, name='add-client'),
    path('clients/show-client/<int:client_id>/', views.show_client, name='show-client'),
    path('clients/edit-client/<client_id>/', views.edit_client, name='edit-client'),
    path('clients/del-client/<int:client_id>/', views.del_client, name='del-client'),
    path('clients/opinions/', views.opinions, name='opinions'),
    path('clients/opinions/del-opinion/<int:opinion_id>/', views.del_opinion, name='del-opinion'),
    path('contact/', views.contact, name='contact'),
    path('transaction/', views.transaction, name='transaction'),
    path('transaction/show-transaction/<int:transaction_id>/', views.show_transaction, name='show-transaction'),
    path('transaction/add-transaction/', views.add_transaction, name='add-transaction'),
]