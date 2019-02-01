# odl-ddos-detect

## How to setup environment

open mytopo.py and change the IP address before running

Make sure to change the directory to where mytopo.py is before running the script

```
Start ODL

Start Mininet VM

Run Xming

Open Miniedit in Putty

Enter this into Mininet: sudo python mytopo.py

Pingall to see the topo in ODL gui
```

[Explanation](http://www.takakura.com/Kyoto_data/BenchmarkData-Description-v5.pdf) of attributes for Kyoto University dataset

## TODO List

- [ ] Multithread traffic.py (up to 10 connections at once)

- [ ] Why is Tx pkts double Rx pkts? Tx and Rx should be almost the same

- [ ] Check number of tcp connections

- [ ] Find maximum number of connections before crashes


Run mytopo.py and wait for a host to appear before running datacol_b.py in linux. Stop datacol_b.py before Mininet if you want to keep the last instance of the .json otherwise it will be empty on the last API request.
