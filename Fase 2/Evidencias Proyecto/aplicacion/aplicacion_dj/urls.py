from django.contrib import admin
from django.urls import path
from .views import ficha_lista,servicio_lista, ficha_personal, form_ingreso

urlpatterns = [
    path('ficha_lista/',ficha_lista, name="ficha_lista"),
    path('servicio_lista/', servicio_lista,name="servicio_lista"),
    path('ficha_personal/',ficha_personal,name="ficha_personal"),
    path('form_ingreso/',form_ingreso,name="form_ingreso")

]
