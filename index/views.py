
from django.shortcuts import render

def index (request) :
    return render (request, 'index.html', {})


def plantilla (request) :
    
    datos = {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre': 'Juancho',
    }
     
    return render (request, 'plantilla.html', datos)
