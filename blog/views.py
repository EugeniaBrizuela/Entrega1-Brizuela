from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView, DeleteView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BlogsFormulario
from .models import Blogs

@login_required
def crear_blog (request):
    
    if request.method == 'POST':
      form = BlogsFormulario (request.POST)
      
      if form.is_valid ():
          data = form.cleaned_data
          blog = Blogs (titulo = data ['titulo'], subtitulo = data ['subtitulo'], cuerpo = data ['cuerpo'], imagen = data ['imagen'], resumen = data ['resumen'], autor = data ['autor'], fecha_publicacion = data ['fecha_publicacion'])
          blog.save()
          return redirect ('blog_lista')
      
    form = BlogsFormulario ()      
    return render (request, 'blog/blog_crear.html', {'form': form})



class BlogLista (ListView):
    model = Blogs
    template_name = 'blog/blog_lista.html'
    


class BlogDetalle (DetailView):
    model = Blogs
    template_name = 'blog/blog_detalle.html'



class BlogEditar (LoginRequiredMixin, UpdateView):
    model = Blogs
    success_url = '/blog/pages/'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'resumen', 'autor', 'fecha_publicacion']


class BlogBorrar (LoginRequiredMixin, DeleteView):
    model = Blogs
    success_url = '/blog/pages/'

