from django.urls import path
from .import views 


urlpatterns = [
    path('pages/', views.BlogLista.as_view(), name = 'blog_lista'),
    path('pages/crear/', views.crear_blog, name = 'blog_crear'),
    path('pages/<int:pk>/', views.BlogDetalle.as_view(), name = 'blog_detalle'),
    path('pages/<int:pk>/editar/', views.BlogEditar.as_view(), name = 'blog_editar'),
    path('pages/<int:pk>/borrar/', views.BlogBorrar.as_view(), name = 'blog_borrar')
]
