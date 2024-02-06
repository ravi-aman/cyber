import socket
import subprocess

def get_service_version(ipaddress, port):
    try:
        sock = socket.create_connection((ipaddress, port), timeout=1)
        banner = sock.recv(1024).decode('utf-8').strip()
        sock.close()
        return banner
    except Exception as e:
        return None

def searchsploit(query):
    try:
        result = subprocess.check_output(['searchsploit', query], universal_newlines=True)
        return result.strip()
    except Exception as e:
        return f"Error executing searchsploit: {str(e)}"

ipaddress = input("Enter the IP Address to Scan: ")
ports = int(input("Enter the Ports to Scan (default is 1-1024): "))

def scan(target, ports):
    for port in range(1, ports+1):
        banner = get_service_version(target, port)
        if banner:
            print(f"Port {port} - {banner}")
            
            # Add searchsploit to rate vulnerability
            vulnerability_query = f"{banner.split(' ')[0]} {banner.split(' ')[1]}"
            vulnerability_result = searchsploit(vulnerability_query)
            print(f"Vulnerability Info: {vulnerability_result}")

def ScanTarget(ipaddress, ports):
    if ',' in ipaddress:
        for ip in ipaddress.split(','):
            scan(ip.strip(' '), ports)
    else:
        scan(ipaddress, ports)

ScanTarget(ipaddress, ports)
