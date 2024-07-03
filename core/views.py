from django.shortcuts import render,redirect
from django.contrib.auth.views import logout_then_login
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')

def logout(request):
    return logout_then_login(request,login_url='login')

def registro(request):
       
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    else:
        form = Registro()
        
    return render(request,'registro.html',{"form":form})


def privacidad(request):
     return render(request,'privacidad.html')
 
def terminos(request):
    return render(request, 'terminos.html')

def habitaciones(request):
    habitaciones = Habitacione.objects.all()
    return render(request,'habitaciones.html',{"habitaciones":habitaciones})

def reserva_cliente(request):
        
    return render(request,'reservas.html',{"room":request.session.get("room",[])})

def agregar_reserva(request,codigo):
    
    if not request.user.is_authenticated:
        return redirect(to='login')
    
    room = request.session.get("room",[])
    
    habitacion = Habitacione.objects.get(id_habitacion = codigo)
    
    if room:
        return redirect(to='reservas')
    
    room.append([codigo,habitacion.tipo_habitacion,habitacion.imagen,habitacion.precio,habitacion.cantidad_banios,habitacion.capacidad_persona,habitacion.unidades_disponibles,habitacion.hotel.direccion])
    request.session["room"] = room
    print(codigo)
    
    return redirect(to='reservas')

def borrar_reserva(request):
    request.session["room"] = []
    return redirect(to='habitaciones')

def confirmar_reserva(request):
    carrito = request.session.get("room",[])
    if not carrito:
        return redirect(to='habitaciones')
    
    reserva = Reserva()
    
    
    for item in carrito:
        habitacion = Habitacione.objects.get(id_habitacion = int(item[0]))
        reserva.id_habitacion = habitacion
        reserva.id_hotel = habitacion.hotel
        reserva.propietario = request.user.first_name + " " + request.user.last_name
        reserva.email_propietario = request.user.email
    
    reserva.fono_propietario = request.POST.get("fono")
    reserva.fecha_inicio = request.POST.get("fec-ini")
    reserva.fecha_termino = request.POST.get("fec-ter")
    
    reserva.save()
    
    request.session["room"] = []
    
    return redirect(to='home')
    
    


    
