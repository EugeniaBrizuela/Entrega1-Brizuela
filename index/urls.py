
from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name ='index'),
    path('sobre_nosotras/', views.sobre_nosotras, name ='sobre_nosotras')
]
