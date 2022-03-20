from django.urls import path
from .import views 


urlpatterns = [
    path('crear_blog/', views.crear_blog, name = 'crear_blog'),
    # path('crear_usuario/', views.crear_usuario, name = 'crear_usuario'),
    # path('crear_tienda/', views.crear_tienda, name = 'crear_tienda'),
    # path('lista_tienda/', views.lista_tieda, name = 'lista_tienda')
]
