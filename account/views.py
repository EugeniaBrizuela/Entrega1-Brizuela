from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import NuestroUserForm, EditFullUser
from django.contrib.auth.decorators import login_required
from .models import UserExtension


def mi_login (request):
    
    msj = ''
    
    if request.method == 'POST':
        
        login_form= AuthenticationForm (request, data = request.POST)
        
        if login_form.is_valid ():
            username = login_form.cleaned_data ['username']
            password = login_form.cleaned_data['password']
            
            user = authenticate (username = username, password = password)
            
            # if user is not None ():
                 
            login (request, user)
            return redirect ('index')
                
            # return render(request, 'index/index.html', {'msj': 'Bienvenido '})
        # else:
        #         # msj= 'El usuario no se ha podido autenticar'
        #         return render (request, 'account/login.html', {'login_form': login_form, 'msj': 'El usuario no se pudo autenticar'})
        
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
           return render(request, 'index/index.html', {'msj': f'SE CREÓ CORRECTAMENTE EL USUARIO {username}'})
       
        else:
            return render (request, 'account/registrarse.html', {'form': form, 'msj': 'El formulario no es válido'})
    
    
    form = NuestroUserForm()
    return render (request, 'account/registrarse.html', {'form': form, 'msj': '' })



    

def editar_usuario (request):
    user_extension_logued, _ = UserExtension.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = EditFullUser (request.POST, request.FILES)
        
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            user_extension_logued.avatar = form.cleaned_data['avatar']
            user_extension_logued.link = form.cleaned_data['link']
            user_extension_logued.descripcion = form.cleaned_data['descripcion']
            
            if form.cleaned_data['password1'] != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
                request.user.set_password(form.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()
            
            return redirect('index')
        
        else:
            return render(request, 'account/editar_usuario.html', {'form': form, 'msj': 'El formulario no es válido'})
    
    form = EditFullUser (
        initial={
            'email': request.user.email,
            'password1': '',
            'password2': '',
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
            'descripcion': user_extension_logued.descripcion
        })
    return render(request, 'account/editar_usuario.html', {'form': form})    
    
    
    
  

             