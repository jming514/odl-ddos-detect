# odl-ddos-detect

Explanation of attributes for Kyoto University dataset
http://www.takakura.com/Kyoto_data/BenchmarkData-Description-v5.pdf


1. Generate realistic network traffic / generate attack traffic (hping3)

2. Set idle times for individual flows / access flow data (ODL)

3. Set labels for dataset

4. Train our ML algorithm



Start ODL

Start Mininet VM

Run Xming

Open Miniedit in Putty

Enter this into Miniedit: sudo mn --custom ~/mininet/custom/mytopo.py --topo mytopo --mac --controller=remote,ip=>>YOUR IP<<,port=6633

Pingall to see the topo in ODL gui
