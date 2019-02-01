import json
import requests
import time


def collectData():
    # API request + json dump
    r = requests.get('http://192.168.101.129:8181/restconf/operational/opendaylight-inventory:nodes', auth=('admin', 'admin'))
    data = r.json()
    with open('flowData.json', 'w') as f:
        json.dump(data, f)

    with open('flowData.json', 'r') as f:
        data = json.load(f)

    numOfCon = len(data['nodes']['node'][1]['node-connector'])

    for i in range(numOfCon):
        a = data['nodes']['node'][1]['node-connector'][i]['id']

        if a == 'openflow:2:1':
            b = data['nodes']['node'][1]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['packets']['received']
            c = data['nodes']['node'][1]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['packets']['transmitted']
            d = data['nodes']['node'][1]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['bytes']['received']
            e = data['nodes']['node'][1]['node-connector'][i]['opendaylight-port-statistics:flow-capable-node-connector-statistics']['bytes']['transmitted']

            entry = [a, b, c, d, e]

            with open('flowDataset.txt', 'a') as f:
                for item in entry:
                    f.write('%s\t' % item)
                f.write('\n')
        else:
            pass


if __name__ == '__main__':
    x = 0
    while (x < 120):
        collectData()
        print(x)
        time.sleep(3)
        x += 1
