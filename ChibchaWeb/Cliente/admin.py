from django.contrib import admin
from .models import Cliente, Plan, SitioWeb, TarjetaCredito, Ticket, Caracteristica

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Plan)
admin.site.register(SitioWeb)
admin.site.register(TarjetaCredito)
admin.site.register(Ticket)
admin.site.register(Caracteristica)
