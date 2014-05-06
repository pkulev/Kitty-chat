#! /usr/bin/env python

import sys
import socket
import threading

#example
class ConnectionHeader():
    nickname = ""
    shortnick = ""
    prompt = ""

HOST = "localhost"
PORT = 80

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


serversocket.bind((HOST, PORT))

serversocket.listen(5)

def client_thread(clinetsocket):
    pass

while True:
    (clientsocket, address) = serversocket.accept()
    ct = client_tread(clientsocket)
    ct.run()
