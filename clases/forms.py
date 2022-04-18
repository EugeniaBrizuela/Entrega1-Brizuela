from django import forms
  
    

class ProfesionalFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=50)  



class ConsultasFormulario (forms.Form):
    nombre = forms.CharField (max_length=20)
    apellido = forms.CharField (max_length=30)
    email = forms.EmailField (max_length=50)
    pregunta = forms.CharField (max_length=200)
        
    



class EstudianteFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    carrera = forms.CharField(max_length=50)
    



class EstudianteBusqueda (forms.Form):
    nombre = forms.CharField (max_length=20)
    
       
    