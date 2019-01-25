import json
import requests
import time, threading


# this is run outside of the environment
def collectData():
    # API request + json dump
    # r = requests.get('http://192.168.101.129:8181/restconf/operational/opendaylight-inventory:nodes', auth=('admin', 'admin'))
    # data = r.json()
    # with open('flowData.json', 'w') as f:
    #     json.dump(data, f)

    # read json
    with open('flowData.json', 'r') as f:
        data = json.load(f)

    unwanted_chars = '(){}\'received:transmitted,'

    numOfCon = len(data['nodes']['node'][0]['node-connector'])
    for i in range(numOfCon):
        x = data['nodes']['node'][0]['node-connector'][i]['id']
        y = str(data['nodes']['node'][0]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['packets'])
        z = str(data['nodes']['node'][0]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['bytes'])
        j = str(data['nodes']['node'][0]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['duration']['second'])
        
        for c in unwanted_chars:
            y = y.replace(c, '')
            z = z.replace(c, '')
            j = j.replace(c, '')
        
        # append to a text file
        print(x, y, z, j)
