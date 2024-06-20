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

#def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(to='home')  # Cambia 'home' por la URL a la que quieras redirigir tras el inicio de sesión
            else:
                form.add_error(None, 'Correo electrónico o contraseña incorrectos')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def privacidad(request):
     return render(request,'privacidad.html')
 
def terminos(request):
    return render(request, 'terminos.html')

