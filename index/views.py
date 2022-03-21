
from django.shortcuts import render

def index (request) :
    return render (request, 'index/index.html', {})


def sobre_nosotras (request) :
    
    datos = {
        
    }
     
    return render (request, 'index/sobre_nosotras.html', datos)
