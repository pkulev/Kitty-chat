#! /usr/bin/env python

import sys
import socket

HOST = "localhost"
PORT = 80

serversocket = socket.socket(socket.AF_INET, socket.sock_STREAM)


serversocket.bind((HOST, PORT))

serversocket.listen(5)

while True:
    (clientsocket, address) = serversocket.accept()
    ct = client_tread(clientsocket)
    ct.run()
