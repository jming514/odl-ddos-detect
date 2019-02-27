import json
import requests
import time
import numpy as np
import csv
import pandas as pd
import matplotlib
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from itertools import groupby
from operator import itemgetter
import threading
import random


def collectData():
    # API request + json dump
    r = requests.get('http://192.168.75.128:8181/restconf/operational/opendaylight-inventory:nodes', auth=('admin', 'admin'))
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
            entry1 = [b, c, d, e]
            

            with open('flowDataset.txt', 'a') as f:
                for item in entry:
                    f.write('%s\t' % item)
                f.write('\n')
            with open('flowDataset4.csv', 'a', newline='') as myfile:
                 wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                 wr.writerow(entry1)

            df = pd.read_csv('flowDataset4.csv')
            df.dropna()
            df_out = df.diff()
            df_out = df_out.dropna()
            with open('flowDataset4.csv', 'a', newline='') as myfile:
                 wr = csv.writer(myfile)
                 wr.writerow(df_out)
            
            



                 

                
        else:
            pass

x = pd.read_csv("C:\\Users\\Deep\\Desktop\\odl-ddos-detect\\flowDataset5.csv")
kmeans = KMeans(n_clusters=2) #creating 2 clusters for ddos/notddos
KMmodel = kmeans.fit(x) #initial kmean training
y = KMmodel.labels_
print(KMmodel.labels_)  #printing labels
print(KMmodel.cluster_centers_) #printing values of centers of both clusters
def printit():
  threading.Timer(5.0, printit).start()

  df = pd.read_csv('flowDataset5.csv')
  xnew = df.values[-1].tolist()
  print(xnew)

  ynew = kmeans.predict([xnew]) #error gets bigger and bigger here look into it
  print(ynew)
if __name__ == '__main__':
    x = 0
    while (x < 120):
        collectData()
        print(x)
        printit()
        time.sleep(3)
        x += 1
