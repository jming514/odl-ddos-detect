import socket
import sys
import time
import random
import os
from threading import *

'''
Host waits join_time seconds before creating a socket to server
Host sends msg to the server
Host makes reqConns number of connections to server
Each connection lasts inter_time seconds 

Total duration = x * [join_time + (reqConns * inter_time)]
'''

def nettraffic():
    # run for a long time
    x = 0
    while (x < 15):
        server = '10.0.0.46'
        port = 12345

        # this is the inter-arrival time AND the start time

        join_time = [j * 0.1 for j in range(20, 40)]
        time.sleep(random.choice(join_time))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except:
            print 'Failed to create a socket'
            sys.exit()

        print 'Socket created'

        s.connect((server, port))

        msg = 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'

        # number of GET requests per connection
        y = 0
        reqPerConn = [5, 6, 7]
        reqConns = random.choice(reqPerConn)
        while (y < reqConns):
            s.sendall(msg)
            reply = s.recv(2048)
            print(reply)

            # duration of the connection
            inter_time = [j * 0.1 for j in range(30, 140)]
            time.sleep(random.choice(inter_time))
            y += 1
        x += 1
        s.close()


if __name__ == '__main__':
    print('Running')
    time.sleep(30)

    # each client will have range(x) simultaneous connections to the server
    for i in range(7):
        t = Thread(target=nettraffic)
        t.start()
        time.sleep(0.5)
