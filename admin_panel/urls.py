from django.urls import path
from admin_panel import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.cars, name='cars'),
    path('cars/add-car/', views.add_car, name='add-car'),
    path('cars/del-car/<int:car_id>/', views.del_car, name='del-car'),
    path('cars/edit-car/<car_id>', views.edit_car, name='edit-car'),
    path('clients/', views.clients, name='clients'),
    path('clients/add-client/', views.add_client, name='add-client'),
    path('clients/show-client/<int:client_id>/', views.show_client, name='show-client'),
    path('clients/del-client/<int:client_id>/', views.del_client, name='del-client'),
    path('clients/opinions/', views.opinions, name='opinions'),
    path('clients/opinions/del-opinion/<int:opinion_id>/', views.del_opinion, name='del-opinion'),
    path('contact/', views.contact, name='contact'),
    path('transaction/', views.transaction, name='transaction'),
    path('transaction/add-transaction/', views.add_transaction, name='add-transaction'),
]