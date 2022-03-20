from django.shortcuts import render
from .forms import BlogFormulario, UsuarioFormulario, TiendaFormulario
from .models import Blog, Usuario, Tienda
from django.shortcuts import redirect

def crear_blog (request):
    
    if request.method == 'POST':
    
      form = BlogFormulario (request.POST)
      
      if form.is_valid ():
          data = form.cleaned_data
          blog = Blog (nombre = data ['nombre'], apellido = data ['apellido'], fecha_publicacion = data ['fecha_publicacion'], titulo = data ['titulo'], publicacion = data ['publicacion'])
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