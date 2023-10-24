from django.db import models

# Create your models here.Empleado

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombreEmpleado = models.CharField(verbose_name="nombre", max_length=20)
    fechaNacimientoEmpleado = models.DateField(verbose_name="Fecha de Nacimiento", blank=True, null=True)
    cargoEmpleado = models.CharField(verbose_name="cargoEmpleado", blank=False,max_length=15 )
    inicioContrato = models.DateField(verbose_name="Fecha de Nacimiento", blank=True, null=True)
    telefonoEmpleado = models.CharField(blank=False, max_length=20)
    emailEmpleado = models.CharField(verbose_name="emailEmpleado", max_length=30)
    contraseniaEmpleado = models.CharField(blank=True, null=True, max_length=20)
    
    class Meta:
        ordering = ('nombreEmpleado',)

    def __str__(self) -> str:
        return self.nombreEmpleado
