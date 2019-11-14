#!/usr/bin/python3.6m
import ipaddress
import socket
import csv


## takes a subnet as a list and 
## wite the hostname and IPs to a file 
## plus the total number of hosts 


listnet = ['172.27.212.0/24']
count = 0


for net in listnet:
    net = ipaddress.ip_network(net)
    netlist = list(ipaddress.ip_network(net).hosts())
    for i in netlist:
        i = str(i)
        try:
            dns = socket.gethostbyaddr(i)
            ip_dns = dns[0] + ',' + str(dns[-1])
            ## print(str(dns[0]) + ',' + str(dns[-1]))
            ip_dns1 = ip_dns.replace("['","")
            ip_dns2 = ip_dns1.replace("']","")
            f = open('dns-names.csv', 'a+')
            f.write(ip_dns2 + '\n')
            count = count +1
        except:
            continue
print('\n')
print("there are " + str(count) + " host names.")

