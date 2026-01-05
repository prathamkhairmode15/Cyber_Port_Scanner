import socket
import subprocess
import platform

def detect_os(target):
    try:
        flag = "-n" if platform.system().lower() == "windows" else "-c"
        result = subprocess.check_output(
            ["ping", flag, "1", target],
            stderr=subprocess.STDOUT
        ).decode().upper()

        if "TTL=" in result:
            ttl = int(result.split("TTL=")[1].split()[0])
            if ttl >= 100: return "Windows (likely)"
            if ttl >= 60:  return "Linux / Unix (likely)"
        return "Unknown"
    except:
        return "Unknown"

def scan_ports(target, start_port, end_port):
    open_ports = []
    tagged = []

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)

            if port == 21:
                tagged.append((port, "FTP — insecure if anonymous login enabled"))
            elif port == 22:
                tagged.append((port, "SSH — prefer key authentication"))
            elif port == 23:
                tagged.append((port, "Telnet — avoid, not encrypted"))
            elif port in (80, 443):
                tagged.append((port, "Web server — check HTTPS & headers"))
            elif port == 3389:
                tagged.append((port, "RDP — enforce MFA & strong passwords"))

        s.close()

    return open_ports, tagged
