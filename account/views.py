from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import NuestroUserForm, NuestraEdicionUser
from django.contrib.auth.decorators import login_required

def mi_login (request):
    
    msj = ''
    
    if request.method == 'POST':
        
        login_form= AuthenticationForm (request, data = request.POST)
        
        if login_form.is_valid ():
            username = login_form.cleaned_data.get ('username')
            password = login_form.cleaned_data.get ('password')
            
            user = authenticate (username = username, password = password)
            
            if user is not None ():
                
                login (request, user)
                
                return render(request, 'index/index.html', {'msj': 'Bienvenido {username}'})
                # return redirect ('inicio')
            else:
                # msj= 'El usuario no se ha podido autenticar'
                return render (request, 'account/login.html', {'login_form': login_form, 'msj': 'El usuario no se pudo autenticar'})
        
        else:
            # msj='El formulario no es válido'
            return render (request, 'account/login.html', {'login_form': login_form, 'msj': 'Los datos tienen un formato que no es válido'})
    
  
        
    login_form = AuthenticationForm ()
    return render (request, 'account/login.html', {'login_form': login_form})
    
    
def registrarse (request):
    
    msj = ''
    
    if request.method == 'POST':
        form = NuestroUserForm(request.POST)
        
        if form.is_valid():
           username = form.cleaned_data ['username']
           form.save()
           return render(request, 'inicio/index.html', {'msj': f'Se creó correctamente el usuario {username}'})
       
        else:
            return render (request, 'account/registrarse.html', {'form': form, 'msj': 'El formulario no es válido'})
    
    
    form = NuestroUserForm()
    return render (request, 'account/registrarse.html', {'form': form, 'msj': '' })



    
@login_required

def editar (request):
    
    msj = ''
    
    if request.method == 'POST':
        form = NuestraEdicionUser (request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            logued_user = request.user
            logued_user.email = data.get('email')
            logued_user.nombre = data.get('nombre', '')
            logued_user.apellido = data.get('apellido', '')
            
            if data.get('password1') == data.get('password2') and len(data.get('password1')) > 10:
                
                logued_user.set_password(data.get('password1'))
            
            else:
                msj = 'No se ha modificado el password.'
            
            logued_user.save()
            return render(request, 'inicio/index.html', {'msj': msj })
        
        else:
            return render(request, 'account/editar_user.html', {'form': form, 'msj': ''})
    
    form = NuestraEdicionUser(
        initial={
            'username': request.user.username,
            'first_name': request.user.nombre,
            'last_name': request.user.apellido,
            'email': request.user.email
        })
    return render(request, 'account/editar_user.html', {'form': form, 'msj': ''})

             