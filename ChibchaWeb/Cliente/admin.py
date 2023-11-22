from django.contrib import admin
from .models import Cliente, Plan, SitioWeb, TarjetaCredito, Ticket, Caracteristica, Dominio, Archivo, DominioCancelado

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Plan)
admin.site.register(SitioWeb)
admin.site.register(TarjetaCredito)
admin.site.register(Ticket)
admin.site.register(Caracteristica)
admin.site.register(Dominio)
admin.site.register(Archivo)
admin.site.register(DominioCancelado)
