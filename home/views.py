from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def FAQ(request):
    return render(request, 'FAQ.html', {})

def index(request):
    return render(request, 'index.html', {})

<<<<<<< HEAD
def CarList(request):
    return render(request, 'CarList.html', {})

def Partners(request):
    return render(request, 'Partners.html', {})
=======
def LP(request):
    return render(request, 'partnerzy.html', {})
>>>>>>> a669718d512b5e55b0d1e04e25997ed51698a297
