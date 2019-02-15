import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale
import sklearn.metrics as sm
import pylab as pl
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

ddos = pd.read_csv("testdataset2.csv")
ddos.info()

# x are the features, y are the labels
x = ddos.drop('Column5', axis=1)
y = ddos['Column5']

kmeans = KMeans(n_clusters=2)
KMmodel = kmeans.fit(x)
# KMmodel.labels_
# KMmodel.cluster_centers_
print(KMmodel.labels_)
print(KMmodel.cluster_centers_)
#testing with a new variable
xnew = [[200, 100, 20000, 40000]]
#xnew = sc.transform(xnew)
ynew = kmeans.predict(xnew)
print(ynew)

print(pd.crosstab(y, KMmodel.labels_))  #see how many get labelled as 0 or 1

# pca = PCA(n_components=2).fit(x)
# pca_2d = pca.transform(x)
# for i in range(0, pca_2d.shape[0]):
#     if y[i] == 0:
#         c1 = pl.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
#     elif y[i] == 1:
#         c2 = pl.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
# pl.legend([c1, c2], ['NOT', 'DDOS'])
# pl.title('dataset with 2 clusters and known outcomes')

# pl.show()
