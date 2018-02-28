#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_addr = ('192.168.1.58', 6666)
sock.connect(serv_addr)

message = 'testing message long long'
sock.sendall(message)
