import os, sys
import subprocess

def sistemls():
    comando4 = "speedtest-cli "
    salida4 = os.popen(comando4).read()
    return salida4

def map(ip,mask):
    comando4 = 'nmap -sn '+ip+'/'+mask
    salida4 = os.popen(comando4).read()
    return salida4

def rutas(ip):
    comando4 = 'traceroute '+ip
    salida4 = os.popen(comando4).read()
    return salida4
   
