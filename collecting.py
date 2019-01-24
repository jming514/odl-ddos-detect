import json
import time, threading

# include everything into this function to periodically write data from pull
# requests to a table
# def foo():
#     print(time.ctime())
#     threading.Timer(1, foo).start()

# foo()

# flow, packet received/transmitted, 

with open('flowData2.json', 'r') as f:
    data = json.load(f)

unwanted_chars = '()}{\'received:transmitted,'
print('flow\tpackets received\tpackets transmitted\tbytes received\tbytes transmitted')

for i in range(4):
    x = data['nodes']['node'][0]['node-connector'][i]['id']
    y = data['nodes']['node'][0]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['packets']
    y = str(y)
    for c in unwanted_chars:
        y = y.replace(c,'')
    z = data['nodes']['node'][0]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['bytes']
    z = str(z)
    for c in unwanted_chars:
        z = z.replace(c,'')
    j = data['nodes']['node'][0]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['duration']['second']
    j = str(j)
    for c in unwanted_chars:
        j = j.replace(c,'')
    print(x, y, z, j)

for i in range(3):
    x = data['nodes']['node'][1]['node-connector'][i]['id']
    y = data['nodes']['node'][1]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['packets']
    y = str(y)
    for c in unwanted_chars:
        y = y.replace(c,'')
    z = data['nodes']['node'][1]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['bytes']
    z = str(z)
    for c in unwanted_chars:
        z = z.replace(c,'')
    j = data['nodes']['node'][1]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['duration']['second']
    j = str(j)
    for c in unwanted_chars:
        j = j.replace(c,'')
    print(x, y, z, j)

for i in range(3):
    x = data['nodes']['node'][2]['node-connector'][i]['id']
    y = data['nodes']['node'][2]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['packets']
    y = str(y)
    for c in unwanted_chars:
        y = y.replace(c,'')
    z = data['nodes']['node'][2]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['bytes']
    z = str(z)
    for c in unwanted_chars:
        z = z.replace(c,'')
    j = data['nodes']['node'][2]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['duration']['second']
    j = str(j)
    for c in unwanted_chars:
        j = j.replace(c,'')
    print(x, y, z, j)
