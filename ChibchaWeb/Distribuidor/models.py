from django.db import models

# Create your m, odels here.Distribuidor

class Distribuidor(models.Model):
    distribuidorId = models.AutoField(primary_key=True)
    nombreDistribuidor = models.CharField(verbose_name="nombreDistribuidor", blank=True,max_length=30)
    categoria = models.CharField(verbose_name="categoria", blank=False, max_length=15)
    comision = models.FloatField(verbose_name="comision")

    class Meta:
        ordering = ('nombreDistribuidor',)

    def __str__(self) -> str:
        return self.nombreDistribuidor
