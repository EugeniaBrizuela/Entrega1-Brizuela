from django import forms
from ckeditor.fields import RichTextFormField




class BlogsFormulario (forms.Form):
    titulo = forms.CharField(label='Título', max_length=30)
    subtitulo = forms.CharField(label='Subtítulo', max_length=30)
    cuerpo = RichTextFormField(required=False)
    imagen = forms.ImageField(required=False)
    resumen = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=30)
    fecha_publicacion = forms.DateTimeField()