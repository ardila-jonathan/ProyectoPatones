# Generated by Django 4.2.4 on 2023-10-23 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Distribuidor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distribuidor',
            options={'ordering': ('nombreDistribuidor',)},
        ),
    ]