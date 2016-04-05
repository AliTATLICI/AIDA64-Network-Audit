# -*- coding: utf-8 -*-

from socket import *


def is_up(addr):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(0.01)   
    if not s.connect_ex((addr,135)):    
        s.close()                     
        return 1
    else:
        s.close()

def run(ipsi):
    network = ipsi
    ip_listesi=[]
    print('')
    for ip in range(1,256):    ## 'ping' adresi 192.168.1.1 ile .1.255 arası
        addr = network + str(ip)
        if is_up(addr):
            ip_listesi.append(addr)
            print('%s \t- %s' %(addr, getfqdn(addr)))    
    return ip_listesi
    

if __name__ == '__main__':
   
    run()

    print('Ağ Taraması yapıldı')
