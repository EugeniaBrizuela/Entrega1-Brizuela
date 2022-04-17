
from django.urls import path
from .import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.mi_login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'account/logout.html'), name = 'logout'),
    path('registrarse/', views.registrarse, name= 'registrarse'),
    path('editar/', views.editar, name = 'editar')
    
    
]
