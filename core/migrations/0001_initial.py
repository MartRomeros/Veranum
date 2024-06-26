# Generated by Django 5.0.6 on 2024-06-12 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_provincia', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id_hotel', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('cantidad_habitaciones', models.IntegerField()),
                ('servicios_extras', models.BooleanField()),
                ('id_comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comuna')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='id_provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.provincia'),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('id_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pais')),
            ],
        ),
        migrations.AddField(
            model_name='provincia',
            name='id_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.region'),
        ),
    ]
