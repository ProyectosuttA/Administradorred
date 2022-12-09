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

