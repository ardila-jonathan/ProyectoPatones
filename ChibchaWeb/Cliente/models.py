from django.db import models

# Create your models here. Ciente


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombreCliente = models.CharField(verbose_name="nombre", max_length=20)
    fechaNacimientoCliente = models.DateField(verbose_name="Fecha de Nacimiento", blank=True, null=True)
    emailCliente = models.CharField(verbose_name="emailCliente", max_length=30)
    paisCliente = models.CharField(verbose_name="paisCliente",blank=False, max_length=10)
    ciudadCliente = models.CharField(verbose_name="ciudadCliente", blank=False, max_length=15)
    usuarioCliente = models.CharField(verbose_name="Usuario", max_length=20, null=True)
    contraseniaCliente = models.CharField(blank=True, null=True, max_length=20)
    planCliente = models.CharField(verbose_name="plan",blank=True, null=True, max_length=20)
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
    numeroTarjeta = models.BigIntegerField(blank=False,verbose_name="tarjeta numero",max_length=18)
    cvc = models.IntegerField(blank=False, max_length=3)
    fechaVencimiento = models.CharField(verbose_name="Fecha de vencimiento", blank=False, max_length=10)

    class Meta:
        ordering = ('clienteId',)

    

    def __str__(self) -> str:
        return self.clienteId

class SitioWeb(models.Model):
    webid = models.AutoField(primary_key=True)
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombreDominio = models.CharField(verbose_name="dominio", blank=True, max_length=30)
    fechaSolicitus= models.CharField(verbose_name="Fecha desolicitus", blank=True, max_length=10)
    
    class Meta:
        ordering = ('nombreDominio',)

    def __str__(self) -> str:
        return self.nombreDominio

class Ticket(models.Model):
    ticketid = models.AutoField(primary_key=True)
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField(verbose_name="Descripcion", blank=True, max_length=100)
    estado = models.BooleanField(default=False)

    class Meta:
        ordering = ('ticketid',)

    def __str__(self) -> str:
        return self.ticketid

class paqueteHosting(models.Model):
    paqueteId = models.AutoField(primary_key=True)
    nombrePaquete = models.CharField(verbose_name="Paquete", blank=True, max_length=15)
    plataforma = models.CharField(verbose_name="plataforma", blank=True, max_length=15)

    class Meta:
        ordering = ('nombrePaquete',)

    def __str__(self) -> str:
        return self.nombrePaquete
    




