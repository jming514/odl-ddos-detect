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
    with open('flowData4.json', 'r') as f:
        data = json.load(f)

    b = 0
    c = 0
    d = 0
    e = 0

    while True:
        numOfCon = len(data['nodes']['node'][0]['node-connector'])

        # inerates over every flow for the switch
        for i in range(numOfCon):
            # attributes
            a = data['nodes']['node'][0]['node-connector'][i]['id']
            b = data['nodes']['node'][0]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['packets']['received']
            c = data['nodes']['node'][0]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['packets']['transmitted']
            d = data['nodes']['node'][0]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['bytes']['received']
            e = data['nodes']['node'][0]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['bytes']['transmitted']
            z = data['nodes']['node'][0]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['duration']
            
            entry = [a, b, c, d, e, z]
            # print(entry)

            # # append to a text file
            with open('flowDataset.txt', 'a') as f:
                for item in entry: 
                    f.write("%s\t" % item)
                f.write("\n")

        time.sleep(1)

collectData()
