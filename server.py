import socket
import sys
from thread import *
import threading
import time


host = '10.0.0.46'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(50)
print 'Waiting for a connection...' 

# thread fuction 
def threaded_client(conn): 
    while True:
        data = conn.recv(2048)
        reppp = "hello world"
        time.sleep(5)
        if not data:
            break
        conn.sendall(reppp)
    conn.close()
    print 'BYE BYE ' + addr[0]

while True:
    conn, addr = s.accept()
    print('connected to: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(threaded_client, (conn,))
