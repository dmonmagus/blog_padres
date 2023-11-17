from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.template import loader
from django.http import HttpResponse
from blog.models import Entrada
from blog.forms import EntradaFormulario
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

# Create your views here.
def inicio(request):
    contexto = {}
    http_response = render (
        request=request,
        template_name='index.html',
        context=contexto,
    )
    return http_response

def about(request):
    contexto = {}
    http_response = render (
        request=request,
        template_name='about.html',
        context=contexto,
    )
    return http_response

def pages(request):
    contexto = {
        "entradas": Entrada.objects.all()
        }
    http_response = render (
        request=request,
        template_name='articulos.html',
        context=contexto,
    )
    return http_response

def crear_entrada(request):
   if request.method == "POST":
       formulario = EntradaFormulario(request.POST, request.FILES)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           titulo = data["titulo"]
           subtitulo = data["subtitulo"]
           cuerpo = data["cuerpo"]
           autor = data["autor"]
           imagen = data["imagen"]
           entrada = Entrada(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, imagen=imagen)  # lo crean solo en RAM
           entrada.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('pages')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = EntradaFormulario()
   http_response = render(
       request=request,
       template_name='formulario_entrada.html',
       context={'formulario': formulario}
   )
   return http_response

class EntradaListView(ListView):
    model = Entrada
    template_name = 'articulos.html'

class EntradaCreateView(LoginRequiredMixin, CreateView):
    model = Entrada
    fields = ('titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen')
    success_url = reverse_lazy('Articulos')

    # Así se guarda la info del creador en vistas basadas en clase
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        # Agregamos la información del creador
        self.object.creador = self.request.user
        self.object.save()
        return super().form_valid(form)


class EntradaDetailView(LoginRequiredMixin, DetailView):
    model = Entrada
    success_url = reverse_lazy('Articulos')

    def get_object(self, queryset=None):
        return get_object_or_404(Entrada, slug=self.kwargs['slug'])


class EntradaUpdateView(LoginRequiredMixin, UpdateView):
    model = Entrada
    fields = ('titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen')
    success_url = reverse_lazy('Articulos')


class EntradaDeleteView(LoginRequiredMixin, DeleteView):
    model = Entrada
    success_url = reverse_lazy('Articulos')
