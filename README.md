# odl-ddos-detect

## How to setup environment

open mytopo.py and change the IP address before running

Make sure to change the directory to where mytopo.py is before running the script

There are 3 separate traffic files because group A B and C are diffferent. There is a maximum of 10*5 + 15*7 + 17*10 = 325

~#24

     hping3 10.0.0.46 -p 12345 -S -i u33000 -c 450               # h44 h45

~#58

     hping3 10.0.0.46 -p 12345 -S -i u14285 -c 1050              # h44 

~#58

     hping3 10.0.0.46 -p 12345 -S -i u11111 -c 1350              # h45

~#98

     hping3 10.0.0.46 -p 12345 -S -i u10000 -c 1500              # h44 h45
```
Start ODL

Start Mininet VM

Run Xming

Open Miniedit in Putty

Enter this into Mininet: sudo python mytopo.py
```

[Explanation](http://www.takakura.com/Kyoto_data/BenchmarkData-Description-v5.pdf) of attributes for Kyoto University dataset

## TODO List

- [ ] Final report

- [ ] false positive/negative test

- [ ] 

- [x] Multithread traffic.py (up to 10 connections at once) || Currently running 5 connections a once

- [x] Move hping3 SYN attacks from topology script to CLI for better control of when attacks appear in dataset

- [x] (A) -> (A + B) -> (A + B + C) <-- volume of traffic timeline || 10 hosts, 25 hosts, 43 hosts. ~~Maybe try stopping ~10 hosts after? This should all be done in mytopo.py~~

- [x] Why is Tx pkts double Rx pkts? Tx and Rx should be almost the same || Same results with rewritten server.py BUT 0207 results are fixed??

- [x] ~~Find maximum number of connections before crashes~~ || 45 hosts with 5 threaded connections possible


Steps for running:

sudo python mytopo.py

xterm server

[server] sudo python server.py


~~Run mytopo.py and wait for a host to appear before running datacol_b.py in linux. Stop datacol_b.py before Mininet if you want to keep the last instance of the .json otherwise it will be empty on the last API request.~~
