from django.shortcuts import render
from .forms import BlogFormulario, UsuarioFormulario, TiendaFormulario, TiendaBusqueda, ConsultasFormulario
from .models import Blog, Usuario, Tienda, Consultas
from django.shortcuts import redirect

def crear_blog (request):
    
    if request.method == 'POST':
    
      form = BlogFormulario (request.POST)
      
      if form.is_valid ():
          data = form.cleaned_data
          blog = Blog (nombre = data ['nombre'], apellido = data ['apellido'], titulo = data ['titulo'], publicacion = data ['publicacion'])
          blog.save()
          return redirect ('index')
      
    form = BlogFormulario ()      
    return render (request, 'clases/crear_blog.html', {'form': form})
           
           
           
           
def crear_usuario (request):
    if request.method == 'POST':
    
      form = UsuarioFormulario (request.POST)
      
      if form.is_valid ():
          data = form.cleaned_data
          usuario = Usuario (nombre = data ['nombre'], apellido = data ['apellido'], email = data ['email'], tejedor = data ['tejedor'])
          usuario.save()
          return redirect ('index')
      
    form = UsuarioFormulario ()      
    return render (request, 'clases/crear_usuario.html', {'form': form})


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



def crear_tienda (request):
    if request.method == 'POST':
    
      form = TiendaFormulario (request.POST)
      
      if form.is_valid ():
          data = form.cleaned_data
          tienda = Tienda (nombre = data ['nombre'], precio = data ['precio'], caracteristicas= data ['caracteristicas'], creadora = data ['creadora'])
          tienda.save()
          return redirect ('index')
      
    form = TiendaFormulario ()      
    return render (request, 'clases/crear_tienda.html', {'form': form})



def lista_tienda (request):
    nombre_a_buscar= request.GET.get ('nombre', None)
    
    if nombre_a_buscar is not None:
        
        productos = Tienda.objects.filter (nombre__icontains=nombre_a_buscar)
    else:
        productos = Tienda.objects.all
    
    form = TiendaBusqueda ()
    return render (request, 'clases/lista_tienda.html', {'form': form, 'productos': productos})

