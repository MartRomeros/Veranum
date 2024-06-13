from django.db import models

# Create your models here.
#modelos que se convertiran en tablas de la base de datos

class Pais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_pais = models.ForeignKey(Pais,on_delete=models.CASCADE) #clave foranea

class Provincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE) #clave foranea
    
class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE) #clave foranea

class Hotel(models.Model):
    id_hotel = models.CharField(max_length=5,primary_key=True)
    direccion = models.CharField(max_length=100)
    cantidad_habitaciones = models.IntegerField()
    servicios_extras = models.BooleanField()
    id_comuna = models.ForeignKey(Comuna,models.CASCADE) #clave foranea



