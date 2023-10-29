from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rol(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.CharField(verbose_name="rol", blank=False, max_length=20)