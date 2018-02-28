#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = ''
port = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

while True:
    data, (peer_host, peer_port) = sock.recvfrom(5)
    print data
    if not data:
        break
