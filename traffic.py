import socket
import sys
import time
import random
import os
from threading import *


def nettraffic():
    #
    x = 0
    while (x < 100):
        server = '10.0.0.46'
        port = 12345

        # this is the inter-arrival time AND the start time
        join_time = [0.4, 0.6, 0,9, 1.1, 1.8, 2.0]
        time.sleep(random.choice(join_time))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        except:
            print 'Failed to create a socket'
            sys.exit()

        print 'Socket created' 

        s.connect((server, port))

        # msg = 'GET / HTTP/1.1 \r\n\r\n'
        msg = 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'

        # number of GET requests per connection
        y = 0
        reqPerConn = [5, 6, 7]
        while (y < random.choice(reqPerConn)):
            s.sendall(msg)
            reply = s.recv(2048)
            print(reply)

            # duration of the connection
            inter_time = [1.5, 1.6, 1.7, 1.8, 1.9]
            time.sleep(random.choice(inter_time))
            y += 1
        x + 1
        s.close()
        

if __name__ == '__main__':
    print('Running')
    time.sleep(45)

    # each client will have 5 simultaneous connections to the server
    for i in range(5):
        t = Thread(target=nettraffic)
        t.start()
        time.sleep(0.5)
