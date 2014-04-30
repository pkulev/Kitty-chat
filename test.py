#! /usr/bin/env python
import sys
import socket
import argparse
from datetime import datetime
#LOGGER

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

def die(msg):
    delim = " "
    print(str(datetime.now())+ delim + msg)

die('Creating socket...')

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    die('Failed to create socket: ' + msg[0] + ' ' + msg[1])
    sys.exit()

die(msg='Socket created')

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    die('Hostname could not be resolved. Exitting...')
    sys.exit()

if not host == remote_ip:
    die('IP address of ' + host + ' is ' + remote_ip)

s.connect((remote_ip, port))
die('Socket connected to ' + remote_ip + ':' + str(port))

while True:
    try:
        message = raw_input("-->")
        s.sendall(message)
    except socket.error:
        die("Send failed")
        sys.exit()
    die('Message send successfully')
    reply = s.recv(4096)
    print(reply)

s.close()
