import socket
import subprocess
from _datetime import datetime

target = input("Enter the target website/IP Address: ")

def port_scan(target):
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Scanning the target {target_ip}")
        print(f"Scan Started at", datetime.now())

        for port in range(20,450):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print("Port {} is open".format(port))
            sock.close()
        
        print(f"Scan Ended at", datetime.now())
    
    except socket.gaierror:
        print("Hostname could not be resolved")
    except socket.error:
        print("Could not connect to the server")

port_scan(target)