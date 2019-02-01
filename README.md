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

- [x] Generate realistic network traffic / generate attack traffic (hping3)

- [ ] Set idle times for individual flows / access flow data (ODL)

- [ ] Set labels for dataset

- [ ] Train our ML algorithm


traffic.py needs to be modified. mytopo.py includes building the network + running the server + network traffic generation

Run server.py on one thread then sleep for 5 seconds before running network traffic. Attack ~3 seconds after.

Two attacker hosts need to be added to perform SYN flood during network traffic.
