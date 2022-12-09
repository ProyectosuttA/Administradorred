from django.shortcuts import render, redirect
from .sistema import sistemls
from .sistema import map
from .sistema import rutas
from .conexions import *
import os
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .models import Datos


def inicio(request):
    return render (request ,'index.html')

def conexion(request):
    if request.method=='POST':
        Datos.objects.all().delete()
        tipo=request.POST['tipo']
        host=request.POST['ip']
        usuario=request.POST['usuario']
        password=request.POST['password']
        n_conexion=Datos(host=host,user=usuario,tipo=tipo,password=password,pactivo=True)
        n_conexion.save()
        id_regis = n_conexion.id
        conection_active = Datos.objects.get(pactivo=True)     

        valor=cone( conection_active.host, conection_active.user,conection_active.password)
        return render(request, 'conexion.html',{'valor':valor})
        
        
    return render(request, 'conexion.html')

def mapeo(request):
    try:
        if request.method=='POST':
            ip=request.POST['ip']
            mask=request.POST['subred']
            valor=map(ip, mask)
            return render(request, 'mapeo.html',{'valor':valor} )
        else:
            valor=' '
            return render(request, 'mapeo.html', {'valor':valor})
    except:
        return render (request, 'mapeo.html' )


def red(request):
    variable=sistemls()
    return render (request ,'red.html',{'valor':variable})

def imagen(request):
    return render(request, 'imagen.html')

def ruta(request):
    if request.method=='POST':
        ip=request.POST['ip']
        valor=rutas(ip)
        return render(request, 'ruta.html',{'valor':valor} )
    else:
        valor=' '
        return render(request, 'ruta.html',{'valor':valor} )

def acciones(request):
    if request.method=='POST':
        print(request.POST['name'])
        return render (request ,'acciones.html')

    return render (request ,'acciones.html')

def mostrarc(request):
    valor='CONFIGURACIÓN DEL DISPOSITIVO'
    valor1='Muestra la configuración general del dispositivo'
    try:
        conection_active = Datos.objects.get(pactivo=True)
        valor2=cone( conection_active.host, conection_active.user,conection_active.password)
        return render (request, 'formulario.html', {'valor':valor, 'valor1':valor1, 'valor2':valor2 })
    except:
        valor2='Error en la conexion '
        return redirect('acciones')

def mostrarr(request):
    valor='RUTAS'
    valor1='Muestra las rutas de los dispositivos'
    try:
        conection_active = Datos.objects.get(pactivo=True)    
        valor2=rutai(conection_active.host, conection_active.user,conection_active.password)
        return render (request, 'formulario.html', {'valor':valor, 'valor1':valor1, 'valor2':valor2 })
    except:
        valor2='Error en la conexion '
        return redirect('acciones')

def interface(request):
    valor='INTERFACES'
    valor1='Muestra las interfaces'
    try:
        conection_active = Datos.objects.get(pactivo=True)
        valor2=interfaces(conection_active.host, conection_active.user,conection_active.password)
        return render (request, 'formulario.html', {'valor':valor, 'valor1':valor1, 'valor2':valor2 })
    except:
        valor2='Error en la conexion '
        return redirect('acciones')

def registro(request):
    if request.method=='GET':
        return render (request, 'registro.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/')
            except:
                return render (request, 'registro.html',{'form':UserCreationForm, 'valor':'El usuario ya existe'})

        else:
            return render (request, 'registro.html',{'form':UserCreationForm, 'valor':'Las contraseñas no coinciden'})
        
        return render (request, 'registro.html',{'form':UserCreationForm})

def salir(request):
    logout(request)
    Datos.objects.all().delete()
    return redirect('/')

def ingresar(request):
    if request.method=='POST':
        user=authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'ingresar.html',{'form':AuthenticationForm, 'valor':'No existe el usuario'}) 
        else:
            login(request,user)
            return redirect('/')       
    
    else:
        return render(request,'ingresar.html',{'form':AuthenticationForm})   
  
         




# Create your views here.
