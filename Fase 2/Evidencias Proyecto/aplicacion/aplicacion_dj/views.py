from django.shortcuts import render

# Create your views here.
def ficha_lista(request):
    return render(request,"ficha_lista.html")

def servicio_lista(request):
    return render(request, "servicio_lista.html")

def ficha_personal(request):
    return render(request,"ficha_personal.html")

def form_ingreso(request):
    return render(request,"form_ingreso.html")