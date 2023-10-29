from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Empleado
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.

def consulta_empleado(request):
    return render(request, "empleado.html")


def editar_empleado(request, id_empleado):
    pass
