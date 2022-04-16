
from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name ='index'),
    path('sobre_mi/', views.sobre_mi, name ='sobre_mi')
]
