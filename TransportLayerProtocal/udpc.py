#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serv_addr = ('127.0.0.1', 8888)

message = 'testing message'
sock.sendto(message, serv_addr)
