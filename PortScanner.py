#Basic port scanner for python project
#Author: Alexander Nunley

import socket
import threading

target = input("Enter the target IP address: ")
ports = range(1, 1025)

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open")
    except:
        pass

for port in ports:
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()


#Guess what? Still gonna be great.
