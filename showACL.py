#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

import json
import netmiko
import logging
import logging
paramiko_logger = logging.getLogger('paramiko.transport')
if not paramiko_logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter('%(asctime)s | %(levelname)-8s| PARAMIKO: '
                      '%(lineno)03d@%(module)-10s| %(message)s')
    )
paramiko_logger.addHandler(console_handler)

devices = """
10.128.63.254
10.83.250.253
10.83.250.252
10.83.250.251
10.147.250.252
10.35.250.252
10.35.250.251
10.211.250.249
10.147.250.251
10.17.127.254
10.35.250.250
10.64.127.254
10.147.250.250
10.192.191.253
10.35.250.247
10.16.63.254
10.147.250.249
10.83.250.203
10.147.250.248
10.67.63.254
10.35.250.243
10.211.250.246
10.147.250.247
10.147.250.246
10.35.250.240
10.147.250.245
10.147.250.244
10.128.127.254
10.128.191.254
10.83.250.245
10.35.250.239
10.83.250.244
10.192.63.254
10.192.127.254
10.128.255.254
10.65.191.254
10.192.127.253
10.17.255.254
10.35.250.208
10.83.250.200
10.129.63.254
10.147.250.243
10.129.127.254
10.147.250.241
10.129.191.254
10.18.63.254
10.211.250.243
10.83.250.241
10.83.250.240
10.192.191.254
10.66.63.254
10.66.127.254
10.211.250.238
10.211.250.237
10.16.127.254
10.147.250.253
10.147.250.240
10.83.250.231
10.66.191.254
10.18.127.254
10.211.250.236
10.83.250.237
10.192.255.254
10.66.255.254
10.147.250.238
10.35.250.237
10.18.191.254
10.18.255.254
10.211.250.253
10.35.250.236
10.193.63.254
10.65.191.253
10.83.250.234
10.83.250.233
10.193.127.254
10.17.191.254
10.128.255.252
10.211.250.254
10.129.255.253
10.16.191.254
10.130.63.254
10.129.127.252
10.20.127.252
10.64.127.253
10.20.127.254
10.83.250.196
10.35.250.238
10.35.250.193
10.211.250.250
10.211.250.212
10.35.250.199
10.83.250.247
10.147.250.210
10.35.250.203
10.211.250.239
10.211.250.252
10.147.250.212
10.83.250.254
10.208.56.1
10.129.255.254
10.19.64.1
10.35.250.212
""".strip().splitlines()

device_type = 'cisco_ios'
username = 'justin_leopold'
password = 'pwd'

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)

for device in devices:
    try:
        print('~' * 79)
        print('Connecting to device:', device)
        connection = netmiko.ConnectHandler(ip=device, device_type=device_type,
                                            username=username, password=password)
        print(connection.send_command('show access-list Printing-Local-Only'))
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to ', device, e)
