#!/usr/bin/python3.6
## Downlaod Azure json IP file and 
## Parses the Azure and displays the routes received for specific service  
## by region. 

import json
import requests
import wget
import os

url = 'https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20191216.json'

r = requests.get(url)
with open('/home/rfg4/temp/temp01/azure-temp.json', 'wb')  as f:
    f.write(r.content)



x = input('What region name do you want? ')


with open('azure-temp.json', 'r') as json_file:
    data = json.load(json_file)
    for item in data['values']:
        if item['name'] == x:
            print( 'Name: ' + item['name'])
            print("Change Number: " +  str([item['properties']['changeNumber']]))
            print('Total Routes: ' + str(len(item['properties']['addressPrefixes'])))
            for ip in item['properties']['addressPrefixes']:
                print(ip)          
