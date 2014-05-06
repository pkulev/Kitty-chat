#! /usr/bin/env python
import sys
import socket
import argparse
from datetime import datetime
import threading
#LOGGER

#Default global variables for lazy users
IP = "www.google.com"
PORT = 80
QUEUE_SIZE = 5

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--remote', type=str, help="Remote IP or hostname")
parser.add_argument('-p', '--port', type=int, help="Remote port")
parser.add_argument('-q', '--queue', type=int, help="Number of connections")
args = parser.parse_args()

host = args.remote if args.remote else IP
port = args.port if args.port else PORT
queue_size = args.queue if args.queue else QUEUE_SIZE

def log(msg):
    delim = " "
    print(str(datetime.now())+ delim + msg)

log('Creating socket...')

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    log('Failed to create socket: ' + msg[0] + ' ' + msg[1])
    sys.exit()

log(msg='Socket created')

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    log('Hostname could not be resolved. Exitting...')
    sys.exit()

if not host == remote_ip:
    log('IP address of ' + host + ' is ' + remote_ip)


try:
    s.bind((remote_ip, port))
except socket.error as msg:
    log("Bind failed! Error #" + str(msg[0]) + " : " + str(msg[1]))
    sys.exit()

log("Bind is comlete")

s.listen(queue_size)
log("Waiting for connections")

#handling connections
def client_thread(conn):
    greeting = 'Welcome to the kitty server!\n'
    conn.send(greeting.encode('utf-8'))
    while True:
        data = conn.recv(1024).decode('utf-8')
        reply = 'OK...' + data
        if not data:
            break
        conn.sendall(reply.encode('utf-8'))
    conn.close()

while True:
    (conn, addr) = s.accept()
    log('Connected with {0} : {1}'.format(addr[0],addr[1]))
    th = threading.Thread(target=client_thread, args=(conn,))
    th.start()
    th.join()

conn.close()
log('Closing connections...')
s.close()
