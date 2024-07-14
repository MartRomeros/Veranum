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
    path('services',services,name='services'),
    path('habitaciones',habitaciones,name='habitaciones'),
    path('confirmar',confirmar_reserva,name='confirmar'),
    path('misreservas',mis_reservas,name='reservas'),
    path('ubicacion',ubicacion,name='ubicacion'),
    path('cancelar/<codigo>',cancelar_reservas,name='cancelar'),
]
