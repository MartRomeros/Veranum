from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',home,name='home'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',logout,name='logout'),
    path('registro',registro,name='registro'),
    path('privacidad/',privacidad,name='privacidad'),
    path('terminos/',terminos,name='terminos'),
    path('habitaciones',habitaciones,name='habitaciones'),
    path('agregar/<codigo>',agregar_reserva,name='agregar'),
    path('reservas',reserva_cliente,name='reservas'),
    path('borrar',borrar_reserva,name='borrar'),
    path('confirmar',confirmar_reserva,name='confirmar'),
    path('services',services,name='services'),
]
