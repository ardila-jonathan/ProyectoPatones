# Generated by Django 4.2.6 on 2023-11-17 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0016_remove_tarjetacredito_fechavencimientoaño_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjetacredito',
            name='fechaVencimientoAnio',
            field=models.IntegerField(blank=True, null=True, verbose_name='Fecha anio'),
        ),
        migrations.AlterField(
            model_name='tarjetacredito',
            name='fechaVencimientoMes',
            field=models.IntegerField(blank=True, null=True, verbose_name='Fecha mes'),
        ),
    ]