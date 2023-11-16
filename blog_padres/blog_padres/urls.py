"""
URL configuration for blog_padres project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from perfiles.views import registro, login_view, CustomLogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name= "Inicio"),
    path('about/', views.about, name= "Acerca"),
    path('pages/', views.EntradaListView.as_view(), name= "Articulos"),
    path('accounts/login/', login_view, name="login"),
    path('accounts/signup/', registro, name= "Registro"),
    path('accounts/logout/', CustomLogoutView.as_view(), name="logout"),
    path('pages/new-post/', views.EntradaCreateView.as_view(), name="entrada"),
    path('pages/<slug:slug>/', views.EntradaDetailView.as_view(), name= "ver_articulo"),
    path('editar-post/<slug:slug>/', views.EntradaUpdateView.as_view(), name= "editar_articulo"),
    path('borrar-post/<slug:slug>/', views.EntradaDeleteView.as_view(), name= "borrar_articulo")    
]
