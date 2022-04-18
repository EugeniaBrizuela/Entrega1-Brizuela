from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone



class Blogs (models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    cuerpo = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='imagen', null=True)
    resumen = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f'{self.titulo} {self.resumen}'
    