from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here. Ciente

class Caracteristica(models.Model):
    caracteristicaId = models.AutoField(primary_key=True)
    caracteristica = models.TextField(verbose_name="caracteristica", blank=False)

    def __str__(self) -> str:
        return self.caracteristica

class Plan(models.Model):
    planId = models.AutoField(primary_key=True)
    nombrePlan = models.CharField(verbose_name="paquete", blank=True, max_length=20)
    tituloPlan = models.TextField(verbose_name="titulo", blank= False, null=True)
    #plataforma = models.CharField(verbose_name="plataforma", blank=True, max_length=15)
    descripcionPlan = models.TextField(verbose_name="descripcion", blank=False)
    caracteristicasPlan = models.ManyToManyField(Caracteristica)
    precioMensual = models.IntegerField(verbose_name="precio", blank=False)

    class Meta:
        ordering = ('nombrePlan',)

    def __str__(self) -> str:
        return self.nombrePlan

class Cliente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    clienteId = models.AutoField(primary_key=True)
    nombreCliente = models.CharField(verbose_name="nombre", max_length=20)
    fechaNacimientoCliente = models.DateField(verbose_name="Fecha de Nacimiento", blank=True, null=True)
    emailCliente = models.EmailField(verbose_name="emailCliente", max_length=30)
    paisCliente = models.CharField(verbose_name="paisCliente",blank=False, max_length=10)
    ciudadCliente = models.CharField(verbose_name="ciudadCliente", blank=False, max_length=15)
    planId = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    ClienteActivo = models.BooleanField(default=False) 
    last_login = models.DateTimeField(null=True, blank=True)
    is_authenticated = models.BooleanField(default=False)

    def is_authenticated(self):
        return self.is_authenticated
    class Meta:
        ordering = ('nombreCliente',)
        

    def __str__(self) -> str:
        return self.nombreCliente


class TarjetaCredito(models.Model):
    tarjetaId = models.AutoField(primary_key=True)
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numeroTarjeta = models.CharField(blank=False,verbose_name="tarjeta numero",max_length=18, default="NE")
    cvc = models.CharField(blank=False, max_length=3, default="NE")
    fechaVencimiento = models.DateField(verbose_name="Fecha de vencimiento", blank=False, default=datetime.date.today)


class SitioWeb(models.Model):
    webid = models.AutoField(primary_key=True)
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombreDominio = models.CharField(verbose_name="dominio", blank=True, max_length=30)
    fechaSolicitud = models.DateField(verbose_name="Fecha desolicitud",null=True, blank=True, max_length=10)


class Ticket(models.Model):
    ticketid = models.AutoField(primary_key=True)
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField(verbose_name="Descripcion", blank=True, max_length=100)
    estado = models.BooleanField(default=False)


    





    




