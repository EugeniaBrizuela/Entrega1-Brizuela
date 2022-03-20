from django import forms


class BlogFormulario (forms.Form):
    nombre = forms.CharField (max_length=20)
    apellido = forms.CharField (max_length=30)
    fecha_publicacion = forms.DateTimeField ()
    titulo = forms.CharField(max_length=20)
    publicacion = forms.CharField (max_length=100)
    
    

class UsuarioFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField (max_length=50)
    tejedor = forms.BooleanField(required = False)    
    
    



class TiendaFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    precio = forms.IntegerField ()
    caracteristicas = forms.CharField(max_length=100)
    creadora = forms.CharField (max_length=20)



class TiendaBusqueda (forms.Form):
    nombre = forms.CharField (max_length=20)
    
       
    