from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('faq', views.FAQ, name='faq'),
    path('index', views.index, name='index'),
    path('car-list', views.car_list, name='car-list'),
    path('car_list/car_details/<int:car_id>', views.car_details, name='car_details'),
    path('partner-list', views.partner_list, name='partner-list'),
    path('add-opinion', views.add_opinion, name='add-opinion'),
    path('financing', views.financing, name='financing'),
    path('compare/', views.compare, name='compare'),
]