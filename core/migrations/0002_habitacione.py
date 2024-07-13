# Generated by Django 5.0.6 on 2024-07-01 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacione',
            fields=[
                ('id_habitacion', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_habitacion', models.CharField(max_length=100)),
                ('cantidad_banios', models.IntegerField()),
                ('capacidad_persona', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('imagen', models.CharField(max_length=2555)),
                ('unidades_disponibles', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hotel')),
            ],
        ),
    ]