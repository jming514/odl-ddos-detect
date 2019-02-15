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

ddos = pd.read_csv("testdataset2.csv")
ddos.info()


x = pd.read_csv("C:\\Users\\Deep\\Desktop\\odl-ddos-detect\\testdataset3.csv")
kmeans = KMeans(n_clusters=2) #creating 2 clusters for ddos/notddos
KMmodel = kmeans.fit(x) #initial kmean training
y = KMmodel.labels_
print(KMmodel.labels_)  #printing labels
print(KMmodel.cluster_centers_) #printing values of centers of both clusters

#grouping indexes by clusters in order to determine index values of where the ddos happens
groups = [(k, sum(1 for _ in g)) for k, g in groupby(KMmodel.labels_)] 
cursor = 0
result = []
for k, l  in groups:
    if not k and l >= 5:
        result.append([cursor, cursor + l - 1])
    cursor += l



print('The DDOS occurs at flows:')
print(result)

def printit():
  threading.Timer(5.0, printit).start()
  a = random.randrange(200,1600)
  b = random.randrange(300,2000)
  c = random.randrange(1000,100000)
  d = random.randrange(1000,100000)
  xnew = [[a,b,c,d]]
  xnewx = [a,b,c,d]
  
  with open("C:\\Users\\Deep\\Desktop\\odl-ddos-detect\\testdataset3.csv",'a') as fd:
    fd.write("{0}, {1}, {2}, {3}\n".format(xnewx[0], xnewx[1], xnewx[2], xnewx[3]))

   
  x = pd.read_csv("C:\\Users\\Deep\\Desktop\\odl-ddos-detect\\testdataset3.csv")
  kmeans = KMeans(n_clusters=2)
  KMModel = kmeans.fit(x)
  print("*DATA HAS BEEN RE-TRAINED*")
  print(xnew)
  print("*NEW DATA ADDED TO FILE*")
  ynew = kmeans.predict(xnew)
  print(ynew)
  groups = [(k, sum(1 for _ in g)) for k, g in groupby(KMmodel.labels_)] 
  cursor = 0
  result = []
  for k, l  in groups:
    if  not k and l >= 5:
        result.append([cursor, cursor + l - 1])
    cursor += l


  
  print('The DDOS occurs at flows:')
  print(result)
  print('')

printit()
print(pd.crosstab(y,KMmodel.labels_)) #see how many get labelled as 0 or 1






