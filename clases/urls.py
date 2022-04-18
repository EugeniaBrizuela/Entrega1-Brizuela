from django.urls import path
from .import views 


urlpatterns = [
    # path('crear_consultas/', views.crear_consultas, name = 'crear_consultas'),
    path('estudiante/', views.lista_estudiante, name = 'estudiante'),
    path('estudiante/crear/', views.crear_estudiante, name = 'crear_estudiante'),
    path('profesional/', views.ProfesionalLista.as_view(), name = 'profesional_lista'),
    path('profesional/crear/', views.crear_profesional, name = 'profesional_crear'),
    path('profesional/<int:pk>/', views.ProfesionalDetalle.as_view(), name = 'profesional_detalle'),
    path('profesional/<int:pk>/editar/', views.ProfesionalEditar.as_view(), name = 'profesional_editar'),
    path('profesional/<int:pk>/borrar/', views.ProfesionalBorrar.as_view(), name = 'profesional_borrar')
    
]
