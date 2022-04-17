from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NuestroUserForm (UserCreationForm):
    
    email = forms.EmailField ()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        helps_text = {k: '' for k in fields}
        


class NuestraEdicionUser ():
    
    email = forms.EmailField ()
    nombre = forms.CharField (label='Nombre', max_length=20, required=False)
    apellido = forms.CharField (label='Apellido', max_length=30)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'nombre', 'apellido', 'password1', 'password2']
        helps_text = {k: '' for k in fields}   