from scanner import scan_ports
import time

try:
    print("Starting scan on 127.0.0.1 ports 20-100...")
    start_time = time.time()
    ports, tagged = scan_ports("127.0.0.1", 20, 100)
    end_time = time.time()
    print(f"Scan complete in {end_time - start_time:.2f} seconds.")
    print("Open ports:", ports)
    print("Tagged:", tagged)
except Exception as e:
    print("Error:", e)
