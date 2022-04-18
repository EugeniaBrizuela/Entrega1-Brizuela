
from django.shortcuts import render
from .forms import EstudianteFormulario, EstudianteBusqueda, ConsultasFormulario, ProfesionalFormulario
from .models import Profesional, Estudiante, Consultas
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView, DeleteView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
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


@login_required
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

@login_required
def crear_profesional (request):
    if request.method == 'POST':
    
      form = ProfesionalFormulario (request.POST)
      
      if form.is_valid ():
          data = form.cleaned_data
          profesional = Profesional (nombre = data ['nombre'], apellido = data ['apellido'], especialidad = data ['especialidad'])
          profesional.save()
          return redirect ('index')
      
    form = ProfesionalFormulario ()      
    return render (request, 'clases/profesional_crear.html', {'form': form})






class ProfesionalLista (ListView):
    model = Profesional
    template_name = 'clases/profesional_lista.html'
    


class ProfesionalDetalle (DetailView):
    model = Profesional
    template_name = 'clases/profesional_detalle.html'



class ProfesionalEditar (LoginRequiredMixin, UpdateView):
    model = Profesional
    success_url = '/clases/profesional/'
    fields = ['nombre', 'apellido', 'especialidad']


class ProfesionalBorrar (LoginRequiredMixin, DeleteView):
    model = Profesional
    success_url = '/clases/profesional/'



        
        
    

