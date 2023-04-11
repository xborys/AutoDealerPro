from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('login-user/', views.login_user, name='login-user'),
]
