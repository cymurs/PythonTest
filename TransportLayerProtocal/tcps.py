#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = ''
port = 6666

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)
while True:
    conn, addr = sock.accept()

    while True:
        data = conn.recv(3)
        print data
        if not data:
            break
    conn.close()

