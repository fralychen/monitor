#!/usr/bin/python
# -*- coding: UTF-8 -*-
from paramiko import SSHClient
from paramiko import AutoAddPolicy

ip = '47.90.100.35'
prot = 22
user = 'root'
passwd = 'xn275267883*'

cmd = 'pwd'

s = SSHClient()
s.set_missing_host_key_policy(AutoAddPolicy())
s.connect(ip, prot, user, passwd)
stdin,stdout,stderr = s.exec_command(cmd)
print stdout.read()
print stderr.read()
s.close()
