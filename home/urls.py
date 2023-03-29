from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('FAQ', views.FAQ, name='FAQ'),
    path('index', views.index, name='index'),
<<<<<<< HEAD
    path('CarList', views.index, name='CarList'),
    path('Partners', views.Partners, name='Partners')
=======
    path('LP',views.LP,name='LP'),
    
>>>>>>> a669718d512b5e55b0d1e04e25997ed51698a297
]