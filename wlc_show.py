#!/usr/bin/python

## Login into Cisco WLC and write some show commands 
## to a file 

import paramiko
import time
import re



def disable_paging(remote_conn, command="config paging disable", delay=1):
    remote_conn.send(command)
    remote_conn.send("\n")
    time.sleep(delay)

f = open('wlc-output.txt', 'w' )


remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())


remote_conn_pre.connect('wlc-name', username='user', password='pass')

remote_conn = remote_conn_pre.invoke_shell() 

remote_conn.send('user')
remote_conn.send("\n")
remote_conn.send('pass')
remote_conn.send("\n")

output = disable_paging(remote_conn)

remote_conn.send("show client summary")
remote_conn.send("\n")
remote_conn.send("\n")
remote_conn.send("show ap summary")
remote_conn.send("\n")
remote_conn.send("\n")

time.sleep(5)
output = remote_conn.recv(655355) 

f.write(output)
f.close

