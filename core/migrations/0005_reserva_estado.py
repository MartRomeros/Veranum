# Generated by Django 5.0.6 on 2024-07-13 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_reserva_id_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='estado',
            field=models.CharField(default='vigente', max_length=20),
        ),
    ]