# odl-ddos-detect

## How to setup environment

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

1. Generate realistic network traffic / generate attack traffic (hping3)

2. Set idle times for individual flows / access flow data (ODL)

3. Set labels for dataset

4. Train our ML algorithm


traffic.py needs to be modified. mytopo.py includes building the network + running the server + network traffic generation

Two attacker hosts need to be added to perform SYN flood during network traffic.
