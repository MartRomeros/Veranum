from django.shortcuts import render,redirect
from django.contrib.auth.views import logout_then_login
from .forms import *
from .models import *
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

