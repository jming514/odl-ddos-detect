import socket
import sys
import time
import random
import os
from threading import *


def nettraffic():
    # run for a long time
    x = 0
    while (x < 15):
        server = '10.0.0.46'
        port = 12345

        # this is the inter-arrival time AND the start time
        join_time = [0.3, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 2.7, 3.2, 4.4, 5.5, 6.5, 7, 7.5, 8, 9.8, 8.6]
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
        reqPerConn = [5, 5, 6, 6, 6, 7]
        while (y < random.choice(reqPerConn)):
            s.sendall(msg)
            reply = s.recv(2048)
            print(reply)

            # duration of the connection
            inter_time = [1, 2, 2.1, 2.2, 2.3, 3.3, 4.4, 5.5, 6.6, 7.7]
            time.sleep(random.choice(inter_time))
            y += 1
        x + 1
        s.close()
        

if __name__ == '__main__':
    print('Running')
    time.sleep(45)

    # each client will have range(x) simultaneous connections to the server
    for i in range(7):
        t = Thread(target=nettraffic)
        t.start()
        time.sleep(0.5)
