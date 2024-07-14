from django.db import models

# Create your models here.
#modelos que se convertiran en tablas de la base de datos

class Pais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    

class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_pais = models.ForeignKey(Pais,on_delete=models.CASCADE) #clave foranea

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE) #clave foranea

    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE) #clave foranea
    
    def __str__(self):
        return self.nombre

class Hotel(models.Model):
    id_hotel = models.CharField(max_length=5,primary_key=True)
    direccion = models.CharField(max_length=100)
    cantidad_habitaciones = models.IntegerField()
    servicios_extras = models.BooleanField()
    id_comuna = models.ForeignKey(Comuna,models.CASCADE) #clave foranea

    def __str__(self):
        return self.direccion

class Habitacione(models.Model):
    id_habitacion = models.AutoField(primary_key=True)
    tipo_habitacion = models.CharField(max_length=100)
    cantidad_banios = models.IntegerField()
    capacidad_persona = models.IntegerField()
    precio = models.IntegerField()
    imagen = models.CharField(max_length=2555)
    unidades_disponibles = models.IntegerField()
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tipo_habitacion

class Reserva(models.Model):
    cod_reserva = models.AutoField(primary_key=True)
    id_habitacion = models.ForeignKey(Habitacione,on_delete=models.CASCADE)
    propietario = models.CharField(max_length=200)
    email_propietario = models.EmailField(max_length=200)
    fono_propietario = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    estado = models.CharField(max_length=20,default="vigente")
    
    def __str__(self):
        return "reserva numero: " + str(self.cod_reserva) + "(" + self.propietario + ")"
    
    
