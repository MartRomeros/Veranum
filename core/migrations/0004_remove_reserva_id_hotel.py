# Generated by Django 5.0.6 on 2024-07-11 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_reserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='id_hotel',
        ),
    ]
