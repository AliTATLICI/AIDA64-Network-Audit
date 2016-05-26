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

def run(ipsi, liste_sayisi):
    network = ipsi[:9]
    son_ek=int(ipsi[9:])
    ip_listesi=[]
    print('')
    for i in range(int(liste_sayisi)):    ## 'ping' adresi 192.168.1.1 / .1.255
        addr = network + str(son_ek)
        if is_up(addr):
            ip_listesi.append(addr)
            print('%s \t- %s' %(addr, getfqdn(addr)))
        son_ek = son_ek + 1
    return ip_listesi
    


if __name__ == '__main__':
    

    run()

    print('Ağ taraması yapıldı')
