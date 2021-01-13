"""
    sockets=1.0.0
"""
import sys
import socket


def open_ports_scan(ip: str) -> None:
    target = socket.gethostbyname(ip)
    print(f"scanning target: {target} ")
    try:
        PORTS_START = 0
        PORTS_END = 65536
        for port in range(PORTS_START, PORTS_END):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port: {port} is open")
                s.close()
        return
    except:
        print("\nExiting...")
        sys.exit(0)


if __name__ == "__main__":
    ip: str = input('please, enter ip to scan open ports: ')
    open_ports_scan(ip)
