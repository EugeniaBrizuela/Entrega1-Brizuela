from django.shortcuts import render
from .forms import BlogFormulario
from .models import Blog
from django.shortcuts import redirect

# Create your views here.
def crear_blog (request):
    if request.method == 'POST':
    
      form = BlogFormulario (request.POST)
      
      if form.is_valid ():
          data = form.cleaned_data
          blog = Blog (nombre = data ['nombre'], apellido = data ['apellido'], fecha_publicacion = data ['fecha_publicacion'], titulo = data ['titulo'], publicacion = data ['publicacion'])
          blog.save()
          return redirect ('inicio')
      
    form = BlogFormulario ()      
    return render (request, 'clases/crear_blog.html', {'form': form})
           