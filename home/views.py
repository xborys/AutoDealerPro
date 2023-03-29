from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def FAQ(request):
    return render(request, 'FAQ.html', {})

def index(request):
    return render(request, 'index.html', {})

def CarList(request):
    return render(request, 'CarList.html', {})

def LP(request):
    return render(request, 'partnerzy.html', {})

