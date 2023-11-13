from datetime import date
import json
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Archivo, Cliente, TarjetaCredito, Dominio, SitioWeb
from Distribuidor.models import Distribuidor, ExtensionDominio
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def consulta_clientes(request):
    template = loader.get_template('CRUD.html')

    context = {
        "clientes": Cliente.objects.all(),
    }

    return HttpResponse(template.render(context, request))


def consulta_cliente(request):
    return render(request, "cliente.html")

    

@login_required
def editar_cliente(request, id_cliente):
    
    user = request.user
    if user.id == id_cliente:
        if request.method == 'POST':
            
            user.username = request.POST['nuevoUsuario']
            user.save()
            cliente = Cliente.objects.get(usuario_id = id_cliente)
            cliente.nombreCliente = request.POST['nuevoNombre']
            cliente.fechaNacimientoCliente = request.POST['nuevaFechaNacimiento']
            cliente.emailCliente = request.POST['nuevoEmail']
            cliente.paisCliente = request.POST['nuevoPais']
            cliente.ciudadCliente = request.POST['nuevaCiudad']
            cliente.save()
            return redirect('dashboard')
    else:
        return redirect('home')
    return render(request, "editarCliente.html", {'cliente':Cliente.objects.get(usuario_id = id_cliente)})


def cambiar_tarjeta(request):
    user = request.user

    cliente = Cliente.objects.get(usuario = user)

    tarjeta = TarjetaCredito.objects.get(clienteId = cliente)


    return render(request, 'tarjeta.html',{'tarjeta':tarjeta})


@csrf_exempt
def registrarDominio(request):

    if request.method == 'POST':
        user = request.user
        cliente = Cliente.objects.get(usuario = user)
        extensionDominio = ExtensionDominio.objects.get(extensionDominio = request.POST['extension'])
        dominio = Dominio(clienteId = cliente, nombreDominio = request.POST['nombreDominio'],
                          extensionDominio = extensionDominio)
        
        #FALTA VALIDAR EL METODO DE PAGO
        dominio.save()
        return redirect(reverse("registrarDominio"))
    
    else:
        return render(request, 'dominio.html')


@login_required   
def agregarPagina(request, id_cliente):

    user = request.user
    if user.id == id_cliente:
        cliente = Cliente.objects.get(usuario_id = id_cliente)
        id_C= cliente.clienteId
        dominios = Dominio.objects.filter(clienteId_id=id_C, estado='Sin usar').values('nombreDominio','dominioId')
    else:
        return redirect('home')
    
    return render(request, "registroPaginaWeb.html", {'cliente':Cliente.objects.get(usuario_id = id_cliente), 'dominios_disponibles': dominios})

@csrf_exempt
def registrarPaginaWeb(request):
    if request.method == 'POST':
        user = request.user
        cliente = Cliente.objects.get(usuario=user)
        data = json.loads(request.body)
        dominio = data.get('dominio')
        dom=Dominio.objects.get(dominioId = dominio)
        sitio = SitioWeb(clienteId=cliente, nombreDominio=dom.nombreDominio, fechaSolicitud=date.today())
        #actualiza el estado del dominio
        dom.estado='En uso'
        dom.save()
        sitio.save()  # Guardar el objeto SitioWeb en la base de datos

        return JsonResponse({'redirect': '/dashboard'})  # Redirigir a la página de dashboard después de guardar
    else:
        return redirect('home')
   
@csrf_exempt
def registrarPaginaWebArchivo(request):
    if request.method == 'POST':
        user = request.user
        cliente = Cliente.objects.get(usuario=user)
        data = json.loads(request.body)
        dominio = data.get('dominio')
        dom=Dominio.objects.get(dominioId = dominio)
        sitio = SitioWeb(clienteId=cliente, nombreDominio=dom.nombreDominio, fechaSolicitud=date.today())
        #actualiza el estado del dominio
        dom.estado='En uso'
        dom.save()
        sitio.save()  # Guardar el objeto SitioWeb en la base de datos
        #-----------------------
        print(request)
        print(data.get('file_0'))
        for key, file in request.FILES.items():
            nuevo_archivo = Archivo(clienteId=cliente, sitioId=sitio, archivo=file)
            nuevo_archivo.save()



        return JsonResponse({'redirect': '/dashboard'})  # Redirigir a la página de dashboard después de guardar
    else:
        return redirect('home')

def dominiosDisponibles(request, dominio):
    extensiones = ExtensionDominio.objects.all()
    dominios = Dominio.objects.filter(nombreDominio = dominio)
    return render(request,'dominio.html',{'extensiones' : extensiones, 'dominios':dominios, 'dominioObj':dominio})