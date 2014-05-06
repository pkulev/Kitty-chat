#! /usr/bin/env python
import sys
import socket
import argparse
from datetime import datetime
#LOGGER

class Message:
    pass

#Default global variables for lazy users
IP = "www.google.com"
PORT = 80

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--remote', type=str, help="Remote IP or hostname")
parser.add_argument('-p', '--port', type=int, help="Remote port")
args = parser.parse_args()
print(args)

host = args.remote if args.remote else IP
port = args.port if args.port else PORT

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

s.connect((remote_ip, port))
log('Socket connected to ' + remote_ip + ':' + str(port))

while True:
    try:
        message = input("-->")
        s.sendall(message.encode('utf-8'))
    except socket.error:
        log("Send failed")
        sys.exit()
    log('Message send successfully')
    reply = s.recv(4096)
    print(reply)

s.close()
