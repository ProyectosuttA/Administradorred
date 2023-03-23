from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,)

from .models import Datos

def cone(host,user,password):
    
    cisco_router = {
        'device_type': 'cisco_ios',
        'secret': 'cisco',
        'port': 22,
    }
    cisco_router ["host"]=host
    cisco_router ["username"]=user
    cisco_router ["password"]=password
    ssh = ConnectHandler(**cisco_router)

    valor=ssh.send_command('show running-config')
    ssh.disconnect()
    return valor

def rutai(host,user,password):
    
    cisco_router = {
        'device_type': 'cisco_ios',
        'secret': 'cisco',
        'port': 22,
    }
    cisco_router ["host"]=host
    cisco_router ["username"]=user
    cisco_router ["password"]=password

    print(cisco_router)
    ssh = ConnectHandler(**cisco_router)

    valor=ssh.send_command('show ip route')
    ssh.disconnect()
    return valor

def interfaces(host,user,password):
    
    cisco_router = {
        'device_type': 'cisco_ios',
        'secret': 'cisco',
        'port': 22,
    }
    cisco_router ["host"]=host
    cisco_router ["username"]=user
    cisco_router ["password"]=password

    print(cisco_router)
    ssh = ConnectHandler(**cisco_router)

    valor=ssh.send_command('show ip interface brief')
    ssh.disconnect()
    return valor

def cambioi(ip,red, interface  ):
    conection_active = Datos.objects.get(pactivo=True)

    cisco_router = {
        'device_type': 'cisco_ios',
        'secret': 'cisco',
        'port': 22,
    }
    cisco_router ["host"]=conection_active.host
    cisco_router ["username"]=conection_active.user
    cisco_router ["password"]=conection_active.password
    ssh = ConnectHandler(**cisco_router)
    commands = ['end',
            'configure terminal',
            'inter '+ interface,
            'ip address '+ip+' '+red,
            'no shutdown',
            'end']      
    valor=ssh.send_config_set(commands)
    ssh.disconnect()
    return valor

def guardar():
    conection_active = Datos.objects.get(pactivo=True)

    cisco_router = {
        'device_type': 'cisco_ios',
        'secret': 'cisco',
        'port': 22,
    }
    cisco_router ["host"]=conection_active.host
    cisco_router ["username"]=conection_active.user
    cisco_router ["password"]=conection_active.password
    ssh = ConnectHandler(**cisco_router)
    commands = ['end',
        'write',]
    valor=ssh.send_config_set(commands)
    ssh.disconnect()
    return valor

def pings(ip):
    conection_active = Datos.objects.get(pactivo=True)

    cisco_router = {
        'device_type': 'cisco_ios',
        'secret': 'cisco',
        'port': 22,
    }
    cisco_router ["host"]=conection_active.host
    cisco_router ["username"]=conection_active.user
    cisco_router ["password"]=conection_active.password
    ssh = ConnectHandler(**cisco_router)
    commands = ['end',
        'ping '+ip,]
    valor=ssh.send_config_set(commands)
    ssh.disconnect()
    return valor

def nombress(nombre):
    conection_active = Datos.objects.get(pactivo=True)

    cisco_router = {
        'device_type': 'cisco_ios',
        'secret': 'cisco',
        'port': 22,
    }
    cisco_router ["host"]=conection_active.host
    cisco_router ["username"]=conection_active.user
    cisco_router ["password"]=conection_active.password
    ssh = ConnectHandler(**cisco_router)
    commands = ['end',
            'configure terminal',
            'host '+ nombre,
            'end']      
    valor=ssh.send_config_set(commands)
    ssh.disconnect()
    return valor   

def vlans(numero, nombre, ip, red):
    conection_active = Datos.objects.get(pactivo=True)

    cisco_router = {
        'device_type': 'cisco_ios',
        'secret': 'cisco',
        'port': 22,
    }
    cisco_router ["host"]=conection_active.host
    cisco_router ["username"]=conection_active.user
    cisco_router ["password"]=conection_active.password
    ssh = ConnectHandler(**cisco_router)
    commands = ['end',
            'configure terminal',
            'vlan '+numero,
            'name '+nombre,
            'interface vlan '+numero,
            'ip address  '+ip+ ' '+red,
            'no shutdown ',
            'end']      
    valor=ssh.send_config_set(commands)
    ssh.disconnect()
    return valor 

def avlans(inter, numero):
    conection_active = Datos.objects.get(pactivo=True)

    cisco_router = {
        'device_type': 'cisco_ios',
        'secret': 'cisco',
        'port': 22,
    }
    cisco_router ["host"]=conection_active.host
    cisco_router ["username"]=conection_active.user
    cisco_router ["password"]=conection_active.password
    ssh = ConnectHandler(**cisco_router)
    commands = ['end',
            'configure terminal',
            'interface '+inter,
            'switchport mode access ',
            'switchport acces vlan '+numero,
            'no shutdown ',
            'end']      
    valor=ssh.send_config_set(commands)
    ssh.disconnect()
    return valor 


