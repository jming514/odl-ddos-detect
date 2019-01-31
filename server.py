import socket
import sys
from thread import *
import threading


print_lock = threading.Lock() 
  
# thread fuction 
def threaded(c): 
    while True: 
  
        # data received from client 
        data = c.recv(1024) 
        if not data: 
            print('Bye') 
              
            # lock released on exit 
            print_lock.release() 
            break
  
        # reverse the given string from client 
        data = data[::-1] 
  
        # send back reversed string to client 
        c.send(data) 
  
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "10.0.0.46" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror():
        print 'hostname could not be resolved. exiting'
        sys.exit()

    s.bind((remote_ip, port)) 
    print(host, port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print 'socket is listening'
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        print_lock.acquire() 
        print 'Connected to : ' + str(addr[0]) + ': ' + str(addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 