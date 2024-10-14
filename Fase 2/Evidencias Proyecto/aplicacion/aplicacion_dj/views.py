from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def login(request):
    return render(request, 'app/login.html')

def ficha_personal(request):
    return render(request='app/ficha_persola.html')

def form_ingreso(request):
    return render(request='app/form_ingreso.html')

def ficha_lista(request):
    return render(request='app/ficha_lista.html')

def servicio_lista(request):
    return render(request='app/servicio_lista.html')
