import socket
from IPy import IP


def scan(ip_addr, from_port, to_port):

    converted_ip = check_ip(ip_addr)
    print('\n' + '[- Scanning Target]'+str(ip_addr))
    for port in range(int(from_port), int(to_port)):
        scan_port(converted_ip, port)


def grab_banner(s):
    return s.recv(1024)


def scan_port(ip_addr, port):

    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip_addr, port))

        try:
            banner = grab_banner(sock)
            print('[+] Open Port' + str(port) + ':' +
                  str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port' + str(port))
    except:
        pass


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


Targets = input('[+] Enter Url or Ip to scan (split target with [,] :')
port_range_From = input('[+] Enter Port from --> :')
port_range_To = input('[+] Enter Port To <---to :')

if ',' in Targets:
    for ip_addr in Targets.split(','):
        scan(ip_addr.strip(' '), port_range_From, port_range_To)


else:
    scan(Targets, port_range_From, port_range_To)
