from django.db import models

# Create your models here.

class Blog (models.Model):
    nombre = models.CharField (max_length=20)
    apellido = models.CharField (max_length=30)
    fecha_publicacion = models.DateTimeField ()
    titulo = models.CharField(max_length=20)
    publicacion = models.TextField (max_length=100)

    def __self__ ():
        return f'{self.nombre} {self.apellido} {self.titulo}'
        
    
    
class Usuario (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField (max_length=50)
    tejedor = models.BooleanField()
    
    def __self__ ():
        return f'{self.nombre} {self.apellido}'

    
class Tienda (models.Model):
   nombre = models.CharField(max_length=20)
   precio = models.IntegerField ()
   caracteristicas = models.TextField (max_length=100)
   creadora = models.CharField (max_length=20)
   
   def __self__ ():
       return f'{self.nombre}{self.creadora}'
    

    