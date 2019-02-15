import socket
import sys
import time
import random
import os
from threading import *


def nettraffic():
    # run for a long time
    x = 0
    while (x < 2):
        server = '10.0.0.46'
        port = 12345

        # this is the inter-arrival time AND the start time
        join_time = [0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 2.7, 3.2, 4.4, 5.5, 6.5, 7, 7.5, 8]
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
        reqPerConn = [1, 2, 3, 4, 5]
        while (y < random.choice(reqPerConn)):
            s.sendall(msg)
            reply = s.recv(2048)
            print(reply)

            # duration of the connection
            inter_time = [0.7, 1.1, 1.5, 1.6, 1.7, 2.3, 3, 4.2, 5, 6.3, 7]
            time.sleep(random.choice(inter_time))
            y += 1
        x + 1
        s.close()


if __name__ == '__main__':
    print('Running')
    time.sleep(25)

    # each client will have range(x) simultaneous connections to the server
    for i in range(5):
        t = Thread(target=nettraffic)
        t.start()
        time.sleep(0.5)

    time.sleep(45)

    # for i in range(5):
    #     t = Thread(target=nettraffic)
    #     t.start()
    #     time.sleep(0.5)