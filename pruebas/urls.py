"""pruebas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from acciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registro, name='inicio'),
    path('conexion/', views.conexion, name='conexion'),
    path('mapeo/', views.mapeo, name='mapeo'),
    path('red/', views.red, name='red'),
    path('ruta/', views.ruta, name='ruta'),
    path('imagen/', views.imagen, name='red'),
    path('acciones/', views.acciones, name='acciones'),
    path('mostrarc/', views.mostrarc, name='mostrarc'),
    path('mostrarr/', views.mostrarr, name='mostrarr'),
    path('interface/', views.interface, name='interface'),
    path('registro/', views.registro, name='registro'),
    path('ingresar/', views.ingresar, name='ingresar'),
    path('salir/', views.salir, name='salir'),
    path('cambio/', views.cambio, name='cambio'),
    path('guardar/', views.guardarc, name='guardar'),
    path('ping/', views.ping, name='ping'),
    path('nombre/', views.nombre, name='nombre'),
    path('vlan/', views.vlan, name='vlan'),
    path('avlan/', views.avlan, name='avlan'),
    
    
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]