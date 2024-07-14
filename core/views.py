from django.shortcuts import render,redirect
from django.contrib.auth.views import logout_then_login
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')

def logout(request):
    return logout_then_login(request,login_url='login')

def registro(request):
       
    if request.method == "POST":
        
        nombre = request.POST.get("first_name")
        email = request.POST.get("email")
        form = Registro(request.POST)
        
        if form.is_valid(): 
            form.save()
            subject = 'Bienvenido a nuestra plataforma'
            message = f'Hola {nombre},\n\nTu registro ha sido confimado con exito, Gracias por confiar en nuestro equipo.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            
            send_mail(subject, message, email_from, recipient_list)
            return redirect(to='login')
    else:
        form = Registro()
        
    return render(request,'registro.html',{"form":form})


def privacidad(request):
     return render(request,'privacidad.html')
 
def terminos(request):
    return render(request, 'terminos.html')

def services(request):
    return render(request,'servicios.html')

def ubicacion(request):
    return render(request,"ubicacion.html")

def habitaciones(request):
    habitaciones = Habitacione.objects.all()
    reservas = Reserva.objects.filter(email_propietario = request.user.email)
    
    return render(request,'habitaciones.html',{"habitaciones":habitaciones,
                                               "reservas":reservas})


def confirmar_reserva(request):
    nombre = request.user.first_name + " " + request.user.last_name
    email = request.user.email
    
    reservas = Reserva.objects.filter(email_propietario = request.user.email)
    
    for reserva in reservas:
        if reserva.estado == "vigente":
            return redirect(to='reservas')
    
    
    if request.method == "POST":
        name = request.POST.get("valor-name")
        habitacion = Habitacione.objects.get(tipo_habitacion = name)
        habitacion.unidades_disponibles = habitacion.unidades_disponibles - 1
        habitacion.save()
        reserva = Reserva()
        reserva.id_habitacion = habitacion
        reserva.propietario = request.user.first_name + " " + request.user.last_name
        reserva.email_propietario = request.user.email
        reserva.fono_propietario = request.POST.get("fono")
        reserva.fecha_inicio = request.POST.get("fec-ini")
        reserva.fecha_termino = request.POST.get("fec-ter")
        reserva.save()
        
        subject = 'Veranum'
        message = f'Hola {nombre},\n\nTu Reserva ha sido exitosa!\nNumero de reserva: {reserva.cod_reserva}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]            
        send_mail(subject, message, email_from, recipient_list)
    
    return redirect(to='reservas')


def mis_reservas(request):
    if not request.user.is_authenticated:
        return redirect(to='login')
    
    reservas = Reserva.objects.filter(propietario = request.user.first_name + " " + request.user.last_name).order_by("-id_habitacion")
    return render(request,"reservas.html",{"reservas":reservas})

def cancelar_reservas(request,codigo):
    reserva = Reserva.objects.get(cod_reserva = codigo)
    reserva.estado = "cancelada"
    reserva.save()
    habitacion = Habitacione.objects.get(tipo_habitacion = reserva.id_habitacion)
    habitacion.unidades_disponibles = habitacion.unidades_disponibles + 1
    habitacion.save()

    subject = 'Veranum'
    message = f'Hola {request.user.first_name},\n\n¡Tu reserva ha sido cancelada!\nNumero de reserva: {reserva.cod_reserva}\nPorfavor informar si tuvo algun inconveniente con nuestro equipo.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]            
    send_mail(subject, message, email_from, recipient_list)

    return redirect(to='reservas')
        


    
    


    
