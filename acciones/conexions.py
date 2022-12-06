from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,)

def cone(host,user,password):
    
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

    valor=ssh.send_command('show running-config')
    return valor

def show_vlan():
    return 3

def show_ipbrief():
    return 6

def ip():
    return 7



