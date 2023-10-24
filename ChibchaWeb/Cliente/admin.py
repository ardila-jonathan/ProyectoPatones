from django.contrib import admin
from .models import Cliente, paqueteHosting, SitioWeb, TarjetaCredito, Ticket

# Register your models here.
admin.site.register(Cliente)
admin.site.register(paqueteHosting)
admin.site.register(SitioWeb)
admin.site.register(TarjetaCredito)
admin.site.register(Ticket)
