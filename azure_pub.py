#!/usr/bin/python3.6
## Downlaod Azure json IP file and 
## Parses the Azure and displays the routes received for specific service  
## by region. 

import json
import requests

url = 'https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20191216.json'

r = requests.get(url)
with open('/home/rfg4/temp/temp01/azure-temp.json', 'wb')  as f:
    f.write(r.content)



x = input('What region name do you want, a example - Storage.CentralUS? ')


with open('azure-temp.json', 'r') as json_file:
    data = json.load(json_file)
    for item in data['values']:
        if item['name'] == x:
            print( 'Name: ' + item['name'])
            print("Change Number: " +  str([item['properties']['changeNumber']]))
            print('Total Routes: ' + str(len(item['properties']['addressPrefixes'])))
            for ip in item['properties']['addressPrefixes']:
                # remove comment to convert cidr notation to subnet mask notation
                # ip = ip.replace('/32',' 255.255.255.255')
                # ip = ip.replace('/31',' 255.255.255.254')
                # ip = ip.replace('/30',' 255.255.255.252')
                # ip = ip.replace('/29',' 255.255.255.248')
                # ip = ip.replace('/28',' 255.255.255.240')
                # ip = ip.replace('/27',' 255.255.255.224')
                # ip = ip.replace('/26',' 255.255.255.192')
                # ip = ip.replace('/25',' 255.255.255.128')
                # ip = ip.replace('/24',' 255.255.255.0')
                # ip = ip.replace('/23',' 255.255.254.0')
                # ip = ip.replace('/22',' 255.255.252.0')
                # ip = ip.replace('/21',' 255.255.248.0')
                # ip = ip.replace('/20',' 255.255.240.0')
                # ip = ip.replace('/19',' 255.255.224.0')
                # ip = ip.replace('/18',' 255.255.192.0')
                # ip = ip.replace('/17',' 255.255.128.0')
                # ip = ip.replace('/16',' 255.255.0.0')
                # ip = ip.replace('/15',' 255.254.0.0')
                # ip = ip.replace('/14',' 255.252.0.0')
                # ip = ip.replace('/13',' 255.248.0.0')
                # ip = ip.replace('/12',' 255.240.0.0')
                # ip = ip.replace('/11',' 255.224.0.0')
                # ip = ip.replace('/10',' 255.192.0.0')
                # ip = ip.replace('/9',' 255.128.0.0')
                # ip = ip.replace('/8',' 255.0.0.0')
                print(ip)
        



