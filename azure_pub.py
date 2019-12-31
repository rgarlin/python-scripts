#!/usr/bin/python3.6
## Parses the Azure json file and displays the routes received 
## by region. 

import json

x = input('What region name do you want? ')

with open('azure-public-ip.json', 'r') as json_file:
    data = json.load(json_file)
    for item in data['values']:
        if item['name'] == x:
            print( 'Name: ' + item['name'])
            print("Change Number: " +  str([item['properties']['changeNumber']]))
            print('Total Routes: ' + str(len(item['properties']['addressPrefixes'])))
            for ip in item['properties']['addressPrefixes']:
                print(ip)
          
