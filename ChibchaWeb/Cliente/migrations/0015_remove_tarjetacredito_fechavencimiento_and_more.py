# Generated by Django 4.2.6 on 2023-11-17 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0014_dominio_fechacancelacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjetacredito',
            name='fechaVencimiento',
        ),
        migrations.AddField(
            model_name='tarjetacredito',
            name='fechaVencimientoAño',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha de vencimiento año'),
        ),
        migrations.AddField(
            model_name='tarjetacredito',
            name='fechaVencimientoMes',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha de vencimiento mes'),
        ),
    ]