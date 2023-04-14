from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .models import *

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('admin_panel:home'))

        else:
            messages.success(request, 'Wprowadzono nieprawidłowy login lub hasło')
            return redirect('members:login-user')
        
    else:
        return render(request, 'authenticate/login-user.html', {})

    