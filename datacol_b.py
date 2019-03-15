import json
import requests
import time
import numpy as np
import csv
import pandas as pd
import matplotlib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from itertools import groupby
from operator import itemgetter
import threading
import random
from sklearn import metrics

somevar = [0, 0]

# x = pd.read_csv("C:\\Users\\Deep\\Desktop\\odl-ddos-detect\\flowDataset5.csv")
# x.dropna()
ddos = pd.read_csv("C:\\Users\\Deep\\Desktop\\odl-ddos-detect\\flowDataset6.csv")
x = ddos.drop("Column5", axis=1)
y = ddos["Column5"]
sc = StandardScaler()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
x_train = sc.fit_transform(x_train)


def kmeans():
    kmeans = KMeans(n_clusters=2)  # creating 2 clusters for ddos/notddos
    KMmodel = kmeans.fit(x)  # initial kmean training
    y = KMmodel.labels_
    print(y)  # printing labels
    print(KMmodel.cluster_centers_)  # printing values of centers of both clusters


def Randomforest(x1):
    rfc = RandomForestClassifier(n_estimators=200)  # how many trees in forest
    rfc.fit(x_train, y_train)
    pred_rfc = rfc.predict(x1)
    # print(classification_report(y_test,pred_rfc))
    # print('This models accuracy is:')
    # print(accuracy_score(y_test,pred_rfc))

    return pred_rfc


def collectData():
    # API request + json dump
    r = requests.get(
        "http://192.168.75.128:8181/restconf/operational/opendaylight-inventory:nodes",
        auth=("admin", "admin"),
    )
    data = r.json()
    with open("flowData.json", "w") as f:
        json.dump(data, f)

    with open("flowData.json", "r") as f:
        data = json.load(f)

    numOfCon = len(data["nodes"]["node"][1]["node-connector"])

    for i in range(numOfCon):
        a = data["nodes"]["node"][1]["node-connector"][i]["id"]

        if a == "openflow:2:1":
            b = data["nodes"]["node"][1]["node-connector"][i][
                "opendaylight-port-statistics:flow-capable-node-connector-statistics"
            ]["packets"]["received"]
            c = data["nodes"]["node"][1]["node-connector"][i][
                "opendaylight-port-statistics:flow-capable-node-connector-statistics"
            ]["packets"]["transmitted"]
            d = data["nodes"]["node"][1]["node-connector"][i][
                "opendaylight-port-statistics:flow-capable-node-connector-statistics"
            ]["bytes"]["received"]
            e = data["nodes"]["node"][1]["node-connector"][i][
                "opendaylight-port-statistics:flow-capable-node-connector-statistics"
            ]["bytes"]["transmitted"]

            entry = [a, b, c, d, e]
            entry1 = [b, c, d, e]

            with open("flowDataset.txt", "a") as f:
                for item in entry:
                    f.write("%s\t" % item)
                f.write("\n")

            with open("flowDataset4.csv", "a", newline="") as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(entry1)

            df = pd.read_csv("flowDataset4.csv")
            df = df.dropna()
            df_out = df.diff()
            df_out = df_out.dropna()
            # with open('flowDataset4.csv', 'a', newline='') as myfile:
            #     wr = csv.writer(myfile)
            #     wr.writerow(df_out)
            df_out.to_csv("flowDataset5.csv", index=False)
            df3 = pd.read_csv("flowDataset5.csv")
            xnew = df3.values[-1].tolist()
            xnew1 = somevar[0]
            xnew2 = [xnew[0], xnew[1], xnew[2], xnew[3], xnew1]
            with open("flowDataset6.csv", "a", newline="") as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(xnew2)
        else:
            pass


def printit():
    global somevar

    # threading.Timer(5.0, printit).start()

    df = pd.read_csv("flowDataset5.csv")
    x1 = df.values[-1].tolist()
    print(x1)

    x_test1 = sc.transform([x1])
    ynew = Randomforest(x_test1)
    print(ynew)
    somevar = ynew
    # print(metrics.accuracy_score(y_test,pred_rfc))


if __name__ == "__main__":
    x = 0
    while x < 120:
        collectData()
        print(x)
        printit()

        time.sleep(3)
        x += 1
