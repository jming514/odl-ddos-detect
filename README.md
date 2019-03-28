# odl-ddos-detect

## How to setup environment

open mytopo.py and change the IP address before running

Make sure to change the directory to where mytopo.py is before running the script

There are 3 separate traffic files because group A B and C are diffferent. There is a maximum of 10*5 + 15*7 + 17*10 = 325

slowest attack before too many false positives appear

     hping3 10.0.0.46 -p 12345 -S -i u100000 -c 450              # h44 h45
     
```
Start ODL

Start Mininet VM

Run Xming

Open Miniedit in Putty

Enter this into new terminal: sudo python mytopo.py

xterm server

[server] sudo python server.py
```

[Explanation](http://www.takakura.com/Kyoto_data/BenchmarkData-Description-v5.pdf) of attributes for Kyoto University dataset

## TODO List

- [ ] Final report

- [x] false positive/negative test

- [x] Complete live plotting

- [ ] improve GUI

- [ ] change datacol_b and livegraph into modules -> cleaner GUI code

- [ ] try older traffic and see if periodic spikes reappear (current script has spikes again)
