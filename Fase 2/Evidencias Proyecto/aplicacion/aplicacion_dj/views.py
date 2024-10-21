from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "base.html")

def login(request):
    return render(request, "login.html")

def ficha_personal(request):
    return render(request, "ficha_personal.html")

def form_ingreso(request):
    return render(request,'form_ingreso.html')

def ficha_lista(request):
    return render(request,"ficha_lista.html")

def servicio_lista(request):
    return render(request,"servicio_lista.html")
