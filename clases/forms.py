from django import forms


class BlogFormulario (forms.Form):
    nombre = forms.CharField (max_length=20)
    apellido = forms.CharField (max_length=30)
    fecha_publicacion = forms.DateTimeField ()
    titulo = forms.CharField(max_length=20)
    publicacion = forms.CharField (max_length=100)
    
    
    
    

    