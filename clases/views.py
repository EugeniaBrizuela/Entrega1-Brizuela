from django.shortcuts import render
from .forms import ProfesionalFormulario, EstudianteFormulario, EstudianteBusqueda, ConsultasFormulario
from .models import Profesional, Estudiante, Consultas
from django.shortcuts import redirect

           
           
           
           
def crear_profesional (request):
    if request.method == 'POST':
    
      form = ProfesionalFormulario (request.POST)
      
      if form.is_valid ():
          data = form.cleaned_data
          profesional = Profesional (nombre = data ['nombre'], apellido = data ['apellido'], especialidad = data ['especialidad'])
          profesional.save()
          return redirect ('index')
      
    form = ProfesionalFormulario ()      
    return render (request, 'clases/crear_profesional.html', {'form': form})


def crear_consultas (request):
    if request.method == 'POST':
    
      form = ConsultasFormulario (request.POST)
      
      if form.is_valid ():
          data = form.cleaned_data
          consulta = Consultas (nombre = data ['nombre'], apellido = data ['apellido'], email= data ['email'], pregunta = data ['pregunta'])
          consulta.save()
          return redirect ('index')
      
    form = ConsultasFormulario ()      
    return render (request, 'clases/crear_consultas.html', {'form': form})



def crear_estudiante (request):
    if request.method == 'POST':
    
      form = EstudianteFormulario (request.POST)
      
      if form.is_valid ():
          data = form.cleaned_data
          estudiante = Estudiante (nombre = data ['nombre'], apellido = data ['apellido'], carrera = data ['carrera'])
          estudiante.save()
          return redirect ('index')
      
    form = EstudianteFormulario ()      
    return render (request, 'clases/crear_estudiante.html', {'form': form})



def lista_estudiante (request):
    nombre_a_buscar= request.GET.get ('nombre', None)
    
    if nombre_a_buscar is not None:
        
        estudiantes = Estudiante.objects.filter (nombre__icontains=nombre_a_buscar)
    else:
        estudiantes = Estudiante.objects.all
    
    form = EstudianteBusqueda ()
    return render (request, 'clases/lista_estudiante.html', {'form': form, 'estudiantes': estudiantes})

