from django.db import models
from django.utils import timezone

# Create your models here.
class Entrada(models.model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.CharField(max_length=10000)
    autor = models.CharField(max_length=256)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField()