# Generated by Django 4.2.7 on 2023-11-13 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0012_dominio_fechasolicitud_dominio_tiempopropiedad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('archivoId', models.AutoField(primary_key=True, serialize=False)),
                ('archivo', models.FileField(upload_to='archivos/')),
                ('clienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente')),
            ],
        ),
    ]