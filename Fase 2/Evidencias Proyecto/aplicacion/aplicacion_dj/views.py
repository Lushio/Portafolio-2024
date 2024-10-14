from django.shortcuts import render

# Create your views here.
def ficha_lista(request):
    return render(request,"ficha_lista.html")
