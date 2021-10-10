import socket
from IPy import IP


class Port_scan:
    banner = []
    open_ports = []

    def __init__(self, Target_ip, Port_number):
        self.Target_ip = Target_ip
        self.Port_number = Port_number

    def scan(self):
        for port in range(1, int(self.Port_number)):
            self.scan_port(port)

    def scan_port(self, port):

        try:
            converted_ip = self.check_ip()

            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)

            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banner.append(banner)
            except:
                self.banner.append(' ')
            sock.close()
        except:
            pass

    def check_ip(self):
        try:
            IP(self.Target_ip)
            return(self.Target_ip)
        except ValueError:
            return socket.gethostbyname(self.Target_ip)
