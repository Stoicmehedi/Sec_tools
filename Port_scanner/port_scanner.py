import socket
from IPy import IP


def scan(ip_addr, from_port, to_port):
    ip = get_ip(ip_addr)

    print('\n' + '[- Scanning Target]', ip_addr)
    for port in range(from_port, to_port):
        scan_port(ip, port)


def grab_banner(s):
    return s.recv(1024)


def scan_port(ip_addr, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.1)
        if verbose == 'y':
            print('port:', port)
        sock.connect((ip_addr, port))

        try:
            banner = grab_banner(sock)
            print('[+] Open Port', port, ':', str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ', port)
    except:
        pass


def get_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

if __name__ == '__main__':
    Targets = input('[+] Enter Url or Ip to scan (split target with [,]): ')
    start_port, end_port = list(map(int, input('[+] Enter Port Range (Ex. 0-65535): ').split('-')))
    global verbose
    verbose = input('verbose output? (y/n): ')

    if ',' in Targets:
        for ip_addr in Targets.split(','):
            scan(ip_addr.strip(' '), start_port, end_port + 1)
    else:
        scan(Targets, start_port, end_port + 1)