import os
import random
import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

while True:
    data = os.urandom(100)
    s.send(b'N-100')
    time.sleep(3)
    s.send(b'N-100')
    time.sleep(1)

