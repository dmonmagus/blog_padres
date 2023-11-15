from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

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
    contexto = {}
    http_response = render (
        request=request,
        template_name='articulos.html',
        context=contexto,
    )
    return http_response