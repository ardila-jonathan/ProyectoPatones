from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Cliente
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.

def consulta_clientes(request):
    template = loader.get_template('CRUD.html')

    context = {
        "clientes": Cliente.objects.all(),
    }

    return HttpResponse(template.render(context, request))


def consulta_cliente(request):
    return render(request, "cliente.html")


def editar_cliente(request, id_cliente):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST['nuevoUsuario']
        user.save()
        cliente = Cliente.objects.get(clienteId = id_cliente)
        cliente.nombreCliente = request.POST['nuevoNombre']
        cliente.fechaNacimientoCliente = request.POST['nuevaFechaNacimiento']
        cliente.emailCliente = request.POST['nuevoEmail']
        cliente.paisCliente = request.POST['nuevoPais']
        cliente.ciudadCliente = request.POST['nuevaCiudad']
        cliente.save()
        return redirect('dashboard')

    return render(request, "editarCliente.html", {'cliente':Cliente.objects.get(clienteId = id_cliente)})


def cambiar_tarjeta(request):
    return render(request)