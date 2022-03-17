from django.db import models

class Blog (models.Model):
    nombre = models.CharField (max_length=20)
    apellido = models.CharField (max_length=30)
    fecha_publicacion = models.DateField ()
    elemento = models.CharField (max_length=30)
    publicacion = models.TextField (max_length=200)
    
    
class InfoUsuario (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    tejedor = models.BooleanField()
    ocupacion = models.CharField (max_length=40)
    
    
class Tienda (models.Model):
   nombre = models.CharField(max_length=20)
   precio = models.IntegerField ()
   caracteristicas = models.TextField (max_length=50)
   creadora = models.CharField (max_length=20)
   


    