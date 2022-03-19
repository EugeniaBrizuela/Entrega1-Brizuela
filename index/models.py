from django.db import models

class Blog (models.Model):
    nombre = models.CharField (max_length=20)
    apellido = models.CharField (max_length=30)
    fecha_publicacion = models.DateTimeField ()
    titulo = models.CharField(max_length=20)
    publicacion = models.TextField (max_length=100)


    
    
class InfoUsuario (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField ()
    ocupacion = models.CharField (max_length=40)
    


    
class Tienda (models.Model):
   nombre = models.CharField(max_length=20)
   precio = models.IntegerField ()
   caracteristicas = models.TextField (max_length=50)
   creadora = models.CharField (max_length=20)
   


    