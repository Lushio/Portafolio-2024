from django.urls import path
from .views import home, login, ficha_personal, form_ingreso, ficha_lista, servicio_lista

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('ficha_personal/', ficha_personal, name="ficha_personal"),
    path('form_ingreso/', form_ingreso, name="form_ingreso"),
    path('ficha_lista', ficha_lista, name="ficha_lista"),
    path('servicio_lista', servicio_lista, name="servicio_lista"),
]
