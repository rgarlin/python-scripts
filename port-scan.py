#!/usr/bin/python3.6


##########################
## excutes a port scan on a specific subnet  
###########################


import nmap


nm = nmap.PortScanner() # instantiate nmap.PortScanner object
f = open('output.txt', 'w')

nm.scan(hosts='10.10.10.0/24', arguments='-n -sP')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    f.write('{0}'.format(host))
    f.write('\n')
f.close

