from operator import index
from django.urls import path
from .views import index, plantilla
from .import views 

urlpatterns = [
    path('', views.index, name ='index'),
    path('plantilla/', views.plantilla, name ='plantilla')
]
