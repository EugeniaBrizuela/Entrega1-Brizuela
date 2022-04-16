from django.db import models

# Create your models here.

        
    
    
    
class Profesional (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField (max_length=50)
    
    
    def __str__ (self):
           return f'{self.nombre} {self.apellido}'

   
   
class Consultas (models.Model):
    nombre = models.CharField (max_length=20)
    apellido = models.CharField (max_length=30)
    email = models.EmailField (max_length=50)
    pregunta = models.TextField (max_length=200)
    
    def __str__(self):
        return f'{self.nombre} {self.pregunta}'
    
    
    
        
class Estudiante (models.Model):
   nombre = models.CharField(max_length=20)
   apellido = models.CharField (max_length=30)
   carrera = models.CharField(max_length=50)
   
   def __str__ (self):
        return f'{self.apellido} {self.carrera}'
   
    

    