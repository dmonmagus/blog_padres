from django import forms
from django.utils import timezone

class EntradaFormulario(forms.Form):
    titulo = forms.CharField(required=True, max_length=256)
    subtitulo = forms.IntegerField(required=True, max_value=256)
    cuerpo = forms.CharField(max_length=16000, widget=forms.Textarea)
    autor = forms.CharField(max_length=256)
    fecha = forms.DateField()
    imagen = forms.ImageField(required=False)
