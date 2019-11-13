#!/usr/bin/python3.6m
import ipaddress
import socket



## takes a subnet as a list and 
## prints out a host name

listnet = ['172.27.212.0/24']
count = 0 

for net in listnet:
    net = ipaddress.ip_network(net)
    netlist = list(ipaddress.ip_network(net).hosts())
    for i in netlist:
        i = str(i)
        try:
            dns = socket.gethostbyaddr(i)
            print(str(dns[0]) + ',' + str(dns[-1]))
            count = count +1
        except:
            continue
print("there are " + str(count) + " host names.")
