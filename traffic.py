import socket
import sys
import time
import random
# import numpy
import os

def nettraffic():
    x = 1
    server = '10.0.0.46'
    port = 12345

    while (x < 46):
        join_time = [0.4, 0.6, 0,9, 1.1, 1.8, 2.0]
        time.sleep(random.choice(join_time))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        except:
            print 'Failed to create a socket'
            sys.exit()

        print 'Socket created' 

        s.connect((server, port))
        # msg = 'GET / HTTP/1.1\r\nHost: 10.0.0.46\r\nConnection: close\r\n\r\n'
        msg = 'hello world'
        y = 0
        while (y < 6):
            s.sendall(b'helloworld')
            reply = s.recv(2048)
            print(reply)
            inter_time = [0.9, 1.0, 1.1, 1.2, 1.3, 1.4]
            time.sleep(random.choice(inter_time))
            y += 1
        
        x += 1

if __name__ == '__main__':
    # exec(open('server.py').read())
    print('Running')
    time.sleep(15)
    nettraffic()