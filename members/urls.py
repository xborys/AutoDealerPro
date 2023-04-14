from django.urls import path, include
from . import views

app_name = 'members'

urlpatterns = [
    path('login-user/', views.login_user, name='login-user'),
    path('dashboard/', include('admin_panel.urls', namespace='admin_panel')),
]
