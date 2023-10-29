from django.shortcuts import render, redirect
from django.contrib.auth import login
from Cliente.models import Cliente, Plan
from Empleado.models import Empleado
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Rol


# Create your views here.
def inicioSesion(request):
    if request.method == 'POST':
        username = request.POST['usuarioCliente']
        password = request.POST['contraseniaCliente']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            mensaje_advertencia = "Este usario no existe o la clave es erronea."
            return render(request, 'login.html', {'mensaje_advertencia': mensaje_advertencia})
    return render(request, 'login.html')


def ingresar(request):
    if request.user.is_authenticated:       
        return redirect('dashboard')
    else:
        return render(request, 'login.html')


def singout(request):
    logout(request)
    return redirect('home')

def eliminar_usuario(request):
    request.user.delete()
    return HttpResponseRedirect('index.html')

@login_required
def dashboard_view(request):
    # Esta vista solo es accesible si el usuario ha iniciado sesión
    
    try:
        
        user = request.user
        rol = Rol.objects.get(usuario = user).rol
        
        if rol == "Cliente":
            cliente = Cliente.objects.get(usuario = user)
            return render(request, "cliente.html", {'cliente':cliente})
        elif rol == "Distribuidor":
            #Lo que pasa cuando un distribuidor inicia sesión
            pass
        elif rol == "Empleado":
            #Lo que pasa cuando un empleado inicia sesión
            empleado = Empleado.objects.get(usuario = user)
            return render(request, "empleado.html", {'empleado':empleado})
    except:
        return render(request, "inicio.html")


def registro_clientes(request):

    if request.method == 'POST':

        try:
            user = User.objects.create_user(username = request.POST['user'], password=request.POST['pass'])
            user.save()
            login(request, user)
        except:
            return render(request, 'login.html', {'mensaje_advertencia':"EL NOMBRE DE USUARIO REGISTRADO YA EXISTE. INTENTA CON OTRO"})

        nombre = request.POST['name']
        fecha_nac = request.POST['fecha']
        email = request.POST['email']
        pais = request.POST['countrySelect']
        ciudad = request.POST['citySelect']


        nuevoCliente = Cliente(usuario=user, nombreCliente=nombre, fechaNacimientoCliente=fecha_nac, emailCliente=email,
                               paisCliente=pais, ciudadCliente=ciudad, ClienteActivo=False)

        nuevoCliente.save()

        rol = Rol(usuario = user, rol="Cliente")

        rol.save()

        return redirect('home')
    else:
        return render(request, 'login.html')



def home(request):
    return render(request, "inicio.html")

def acercaDeNos(request):
    return render(request, "acercaDeNos.html")

def planes(request):
    return render(request, "planes.html",{'planes':Plan.objects.all()[:3]})