from netmiko import *

from .models import Datos

def conet(host,user,password):
    
    cisco_router = {
        "device_type": "cisco_ios_telnet",
        'secret': 'cisco',
        'port': 100,
        'protocol':'telnet',
    }
    cisco_router ["host"]=host
    cisco_router ["username"]=user
    cisco_router ["password"]=password
    ssh = ConnectHandler(**cisco_router)

    valor=ssh.send_command('show running-config')
    ssh.disconnect()
    return valor