from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Entrada(models.Model):
    titulo = models.CharField(max_length=256, blank=False)
    subtitulo = models.CharField(max_length=256, blank=False)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=256, null= True)
    fecha = models.DateField(auto_now_add=True, null=True)
    imagen = models.ImageField(upload_to='media/', blank=True, null=True)
    slug = models.SlugField(unique=True, default='default-slug')

    def __len__(self):
        return Entrada.objects.count()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Entrada, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.titulo