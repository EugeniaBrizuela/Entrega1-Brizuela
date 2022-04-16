from django.urls import path
from .import views 


urlpatterns = [
    path('crear_profesional/', views.crear_profesional, name = 'crear_profesional'),
    path('crear_consultas/', views.crear_consultas, name = 'crear_consultas'),
    path('crear_estudiante/', views.crear_estudiante, name = 'crear_estudiante'),
    path('lista_estudiante/', views.lista_estudiante, name = 'lista_estudiante')
]
