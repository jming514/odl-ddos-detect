import json
import requests


r = requests.get('http://192.168.101.129:8181/restconf/operational/opendaylight-inventory:nodes', auth=('admin', 'admin'))

#print r.json()

data = r.json()
with open('flowData.json', 'w') as f:
    json.dump(data, f)


