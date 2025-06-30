import socket

def scan_ports(target, start_port=1, end_port=1024):
    open_ports = []
    print(f"Scanning ports {start_port}-{end_port} on {target}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports
