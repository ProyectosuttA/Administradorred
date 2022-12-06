from django.shortcuts import render, redirect
from .sistema import sistemls
from .sistema import map
from .sistema import rutas
from .conexions import cone

def inicio(request):
    return render (request ,'index.html')

def conexion(request):
    if request.method=='POST':
        tipo=request.POST['tipo']
        host=request.POST['ip']
        usuario=request.POST['usuario']
        password=request.POST['password']
        valor=cone(host,usuario,password)
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
    return render (request, 'formulario.html', {'valor':valor, 'valor1':valor1})

# Create your views here.
