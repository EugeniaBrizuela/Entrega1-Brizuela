from django import forms


class BlogFormulario (forms.Form):
    nombre = forms.CharField (max_length=20)
    apellido = forms.CharField (max_length=30)
    titulo = forms.CharField(max_length=20)
    publicacion = forms.CharField (max_length=300)
    
    

class UsuarioFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField (max_length=50)
    tejedor = forms.BooleanField(required = False)    



class ConsultasFormulario (forms.Form):
    nombre = forms.CharField (max_length=20)
    apellido = forms.CharField (max_length=30)
    email = forms.EmailField (max_length=50)
    pregunta = forms.CharField (max_length=200)
        
    



class TiendaFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    precio = forms.IntegerField ()
    caracteristicas = forms.CharField(max_length=100)
    creadora = forms.CharField (max_length=20)



class TiendaBusqueda (forms.Form):
    nombre = forms.CharField (max_length=20)
    
       
    