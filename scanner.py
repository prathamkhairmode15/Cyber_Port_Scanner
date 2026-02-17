
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

import xml.etree.ElementTree as ET

def scan_ports(target, start_port, end_port):
    open_ports = []
    tagged = []

    try:
        # Construct the optimized nmap command
        # -p: Port range
        # -T4: Aggressive timing (faster)
        # -n: No DNS resolution (faster)
        # --min-rate 1000: Send packets no slower than 1000 per second
        # -oX -: Output XML to stdout
        # --open: Only show open ports (optional but good for clarity)
        command = [
            r"C:\Program Files (x86)\Nmap\nmap.exe",
            target,
            f"-p{start_port}-{end_port}",
            "-T4",
            "-n",
            "--min-rate", "1000",
            "-oX", "-"
        ]

        # On Windows, nmap must be in the system PATH.
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            # If nmap fails, raise exception with stderr
            raise Exception(f"Nmap failed: {stderr.strip()}")

        try:
            if not stdout.strip():
                return [], []

            # Parse XML output
            root = ET.fromstring(stdout)
            
            # Find all host elements (should be one for a single target)
            for host in root.findall("host"):
                ports = host.find("ports")
                if ports is None:
                    continue
                
                for port in ports.findall("port"):
                    state = port.find("state")
                    if state is not None and state.get("state") == "open":
                        portid = int(port.get("portid"))
                        open_ports.append(portid)

        except ET.ParseError as e:
            raise Exception(f"Failed to parse Nmap XML output: {e}. Output snippet: {stdout[:100]}...")

    except FileNotFoundError:
        raise Exception("Nmap executable not found in PATH. Please install Nmap from https://nmap.org/download.html")

    # Sort ports numerically
    open_ports.sort()

    for port in open_ports:
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

    return open_ports, tagged
