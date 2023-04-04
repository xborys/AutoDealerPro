from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('FAQ', views.FAQ, name='FAQ'),
    path('index', views.index, name='index'),
    path('CarList', views.CarList, name='CarList'),
    path('LP',views.LP,name='LP'),
    path('Sale_Transaction',views.Sale_Transaction,name='Sale_Transaction'),
    path('add_client',views.Add_Clients,name='add_client'),
    path('ClientsList',views.ClientsList,name='ClientsList'),
]