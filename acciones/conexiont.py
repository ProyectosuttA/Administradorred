import telnetlib
from .models import Datos
def conexiont():
    conection_active = Datos.objects.get(pactivo=True)
    HOST = conection_active.host
    user = conection_active.user
    password = conection_active.password

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")


    print(tn)
    tn.write(b"show running-config view full \n")
    tn.write(b"\n")
    tn.write(b"exit \n")
    valor=tn.read_all().decode('ascii')
    print(valor)
    return valor

def rutat():
    conection_active = Datos.objects.get(pactivo=True)
    HOST = conection_active.host
    user = conection_active.user
    password = conection_active.password

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")


    print(tn)
    tn.write(b"show ip route \n")
    tn.write(b"\n")
    tn.write(b"\n")
    tn.write(b"exit \n") 
    valor=tn.read_all().decode('ascii')
    print(valor)
    return valor

def intert():
    conection_active = Datos.objects.get(pactivo=True)
    HOST = conection_active.host
    user = conection_active.user
    password = conection_active.password

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")


    print(tn)
    tn.write(b"show ip interface brief  \n")
    tn.write(b"\n")
    tn.write(b"\n")
    tn.write(b"exit \n") 
    valor=tn.read_all().decode('ascii')
    print(valor)
    return valor

def pingt(ip):
    conection_active = Datos.objects.get(pactivo=True)
    HOST = conection_active.host
    user = conection_active.user
    password = conection_active.password

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    #tn.write(b"ping "+ ip.encode('utf-8') + b"\n ")
    tn.write(b"exit \n") 
    valor=tn.read_all().decode('ascii')
    valor='FUNCIÓN INHABILITADA PARA ESTE TIPO DE CONEXIÓN'
    tn.close()
    return valor

def nombret(nombre):
    conection_active = Datos.objects.get(pactivo=True)
    HOST = conection_active.host
    user = conection_active.user
    password = conection_active.password
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"config terminal\n")
    tn.write(b"host " + nombre.encode('utf-8') + b" \n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    valor=tn.read_all().decode('ascii')
    tn.close()
    return valor

def cambiot(ip,red, inter ):
    conection_active = Datos.objects.get(pactivo=True)
    HOST = conection_active.host
    user = conection_active.user
    password = conection_active.password
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"config terminal\n")
    tn.write(b"interface " + inter.encode('utf-8') + b" \n")
    tn.write(b"ip address " + ip.encode('utf-8')+b' '+ red.encode('utf-8')+ b" \n")
    tn.write(b"no shutdown \n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    valor=tn.read_all().decode('ascii')
    tn.close()
    return valor

def guardart():
    conection_active = Datos.objects.get(pactivo=True)
    HOST = conection_active.host
    user = conection_active.user
    password = conection_active.password

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")


    print(tn)
    tn.write(b"write \n")
    tn.write(b"exit \n") 
    valor=tn.read_all().decode('ascii')
    print(valor)
    return valor

def vlant(numero, nombre, ip, red ):
    conection_active = Datos.objects.get(pactivo=True)
    HOST = conection_active.host
    user = conection_active.user
    password = conection_active.password
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"config terminal\n")
    tn.write(b"vlan " + numero.encode('utf-8') + b" \n")    
    tn.write(b"name  " + nombre.encode('utf-8') + b" \n")
    tn.write(b"interface vlan" + numero.encode('utf-8') + b" \n")
    tn.write(b"ip address " + ip.encode('utf-8') + b' '+ red.encode('utf-8')+b" \n")
    tn.write(b"no shutdown \n")
    tn.write(b"end \n")
    tn.write(b"exit\n")
    valor=tn.read_all().decode('ascii')
    tn.close()
    return valor

def avlant(inter, numero):
    conection_active = Datos.objects.get(pactivo=True)
    HOST = conection_active.host
    user = conection_active.user
    password = conection_active.password
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"config terminal\n")
    tn.write(b"interface " + inter.encode('utf-8') + b" \n")    
    tn.write(b"switchport mode access \n")
    tn.write(b"switchport access vlan " + numero.encode('utf-8') + b" \n")
    tn.write(b"no shutdown \n")
    tn.write(b"end \n")
    tn.write(b"exit\n")
    valor=tn.read_all().decode('ascii')
    tn.close()
    return valor


