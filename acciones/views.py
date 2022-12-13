from django.shortcuts import render, redirect
from .sistema import sistemls
from .sistema import map
from .sistema import rutas
from .conexions import *
from .conexiont import *
import os
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Datos


@login_required
def conexion(request):
    if request.method=='POST':
        Datos.objects.all().delete()
        tipo=request.POST['tipo']
        tipo=tipo.lower()
        host=request.POST['ip']
        usuario=request.POST['usuario']
        password=request.POST['password']
        n_conexion=Datos(host=host,user=usuario,tipo=tipo,password=password,pactivo=True)
        n_conexion.save()
        id_regis = n_conexion.id
        conection_active = Datos.objects.get(pactivo=True)  
        try:
            if tipo =='telnet':
                valor=conexiont()
                return render(request, 'conexion.html',{'valor':valor})
            elif tipo=='ssh':
                valor=cone( conection_active.host, conection_active.user,conection_active.password)
                return render(request, 'conexion.html',{'valor':valor})
            else:
                return render(request, 'conexion.html',{'valor':'Asigna un tipo de conexión correcto'})
        except:
            return render(request, 'conexion.html',{'valor':'Error en la conexión'})       
        
    return render(request, 'conexion.html',{'valor':' '})

@login_required
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

@login_required
def red(request):
    variable=sistemls()
    return render (request ,'red.html',{'valor':variable})

@login_required
def imagen(request):
    return render(request, 'imagen.html')

@login_required
def ruta(request):
    if request.method=='POST':
        ip=request.POST['ip']
        valor=rutas(ip)
        return render(request, 'ruta.html',{'valor':valor} )
    else:
        valor=' '
        return render(request, 'ruta.html',{'valor':valor} )

@login_required
def acciones(request):
    if request.method=='POST':
        print(request.POST['name'])
        return render (request ,'acciones.html')

    return render (request ,'acciones.html')

@login_required
def mostrarc(request):
    valor='CONFIGURACIÓN DEL DISPOSITIVO'
    valor1='Muestra la configuración general del dispositivo'
    try:
        conection_active = Datos.objects.get(pactivo=True)
        if conection_active.tipo=='ssh':
            valor2=cone( conection_active.host, conection_active.user,conection_active.password)
            return render (request, 'formulario.html', {'valor':valor, 'valor1':valor1, 'valor2':valor2 })
        else:
            valor2=conexiont()
            return render (request, 'formulario.html', {'valor':valor, 'valor1':valor1, 'valor2':valor2 })
    except:
        valor2='Error en la conexion '
        return redirect('acciones')

@login_required
def mostrarr(request):
    valor='RUTAS'
    valor1='Muestra las rutas de los dispositivos'
    try:
        conection_active = Datos.objects.get(pactivo=True) 
        if conection_active.tipo=='ssh':
            valor2=rutai(conection_active.host, conection_active.user,conection_active.password)
            return render (request, 'formulario.html', {'valor':valor, 'valor1':valor1, 'valor2':valor2 })
        else:
            valor2=rutat()
            return render (request, 'formulario.html', {'valor':valor, 'valor1':valor1, 'valor2':valor2 })
    except:
        valor2='Error en la conexion '
        return redirect('acciones')

@login_required
def interface(request):
    valor='INTERFACES'
    valor1='Muestra las interfaces'
    try:
        conection_active = Datos.objects.get(pactivo=True)
        if conection_active.tipo=='ssh':
            valor2=interfaces(conection_active.host, conection_active.user,conection_active.password)
            return render (request, 'formulario.html', {'valor':valor, 'valor1':valor1, 'valor2':valor2 })
        else:
            valor2=intert()
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
        
  #      return render (request, 'registro.html',{'form':UserCreationForm})

@login_required
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

@login_required  
def cambio(request):
      
    try:
        conection_active = Datos.objects.get(pactivo=True)
        if request.method=='POST':
            ip=request.POST['ip']
            red=request.POST['subred']
            inter=request.POST['interf']
            if conection_active.tipo=='ssh':
                valor=cambioi(ip, red, inter)
                return render(request, 'cambio.html',{'valor':valor})
            else:
                valor=cambiot(ip, red, inter)
                return render(request, 'cambio.html',{'valor':valor})
        else:
            valor=' '
            return render(request, 'cambio.html',{'valor':valor})
    except:
        return redirect('/acciones')


@login_required    
def guardarc(request):
    try:
        conection_active = Datos.objects.get(pactivo=True)
        if conection_active.tipo=='ssh':
            valor=guardar()
            return render(request, 'guardar.html',{'valor':valor})
        else:
            valor=guardart()
            return render(request, 'guardar.html',{'valor':valor})
    except:
        valor='ERROR AL ALMACENAR LA CONFIGURACIÓN'
        return render(request, 'guardar.html',{'valor':valor})

@login_required
def ping(request):
   try:
    conection_active = Datos.objects.get(pactivo=True)     
   except:
    return redirect('acciones')

   try:
    if request.method=='POST':
        ip=request.POST['ip']
        if conection_active.tipo=='ssh':
            valor=pings(ip)
            return render(request, 'ping.html',{'valor':valor} )
        else:
            valor=pingt(ip)
            return render(request, 'ping.html',{'valor':valor} )  
    else:
        valor=' '
        return render(request, 'ping.html',{'valor':valor} )
   except:
        valor='No se ha logrado encontra el dispositivo'
        return render(request, 'ping.html',{'valor':valor} )

@login_required
def nombre(request):
    try:
        conection_active = Datos.objects.get(pactivo=True) 
    except:
        return redirect('acciones')
    try:
     if request.method=='POST':
        nom=request.POST['nombre']
        if conection_active.tipo=='ssh':
            valor=nombress(nom)
            return render(request, 'nombre.html',{'valor':valor} )
        else:
            valor=nombret(nom)
            return render(request, 'nombre.html',{'valor':valor} )  
     else:
        valor=' '
        return render(request, 'nombre.html',{'valor':valor} )
    except:
        valor='No se puedo cambiar el nombre'
        return render(request, 'nombre.html',{'valor':valor} )

@login_required
def vlan(request):
    try:
        conection_active = Datos.objects.get(pactivo=True) 
    except:
        return redirect('acciones')
    conection_active = Datos.objects.get(pactivo=True)  
    if request.method=='POST':
        numero=request.POST['vlan']
        nombre=request.POST['nombre']
        ip=request.POST['ip']
        red=request.POST['red']   
        try:
            if conection_active.tipo=='ssh':
                valor=vlans(numero, nombre,ip,red)
                return render(request, 'vlan.html',{'valor':valor})
            else:
                valor=vlant(numero, nombre,ip,red)
                return render(request, 'vlan.html',{'valor':valor})
        except:
            valor='Error al crear la vlan '
            return render(request, 'vlan.html',{'valor':valor})

    else:
        valor=' '
        return render(request, 'vlan.html',{'valor':valor})

@login_required
def avlan(request):
    try:
        conection_active = Datos.objects.get(pactivo=True) 
    except:
        return redirect('acciones') 
    if request.method=='POST':
        inter=request.POST['inter']  
        nvlan=request.POST['vlan']  
        try:
            if conection_active.tipo=='ssh':
                valor=avlans(inter, nvlan)
                return render(request, 'avlan.html',{'valor':valor})
            else:
                valor=avlant(inter, nvlan)
                return render(request, 'avlan.html',{'valor':valor})
        except:
            valor='Error al designar la vlan  '
            return render(request, 'avlan.html',{'valor':valor})

    else:
        valor=' '
        return render(request, 'avlan.html',{'valor':valor})



# Create your views here.
