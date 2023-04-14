from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    return render(request, 'home.html', 
                  {})