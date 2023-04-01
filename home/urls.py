from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('FAQ', views.FAQ, name='FAQ'),
    path('index', views.index, name='index'),
    path('CarList', views.CarList, name='CarList'),
    path('LP',views.LP,name='LP'),
    path('Transakcje',views.Transakcje,name='Transakcje'),
    path('Clients',views.Clients,name='Clients'),
    path('ClientsList',views.ClientsList,name='ClientsList'),
]