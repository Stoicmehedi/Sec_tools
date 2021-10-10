import port_scanner

target_ip = input('[+] Enter target to Scan for vulnerable open ports :')
port_num = int(input('[+] Enter amounts of ports you want to scan :'))
vul_file = input('Enter vuln file path:')
print('Scanning -->'+target_ip)
print('\n')

Target = port_scanner.Port_scan(target_ip, port_num)
Target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in Target.banner:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print(
                    ' On Port ='+str(Target.open_ports[count]) + ' {+}Vunerable Banner Found: '+banner)
                print('\n')

        count += 1
