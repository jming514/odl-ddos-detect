import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale
import sklearn.metrics as sm
import pylab as pl
from sklearn.decomposition import PCA


'''
#wine = pd.read_csv("C:\\python37\\Lib\\site-packages\\sklearn\\datasets\\data\\winequality-red.csv",sep=';')
ddos = pd.read_csv("C:\\Users\\Deep\\Desktop\\log-60-20.csv",sep=';')
print(ddos.head)
bins = (2,6.5,8)
group_names = ['bad','good']
wine['quality'] = pd.cut(wine['quality'], bins = bins, labels = group_names)
label_quality = LabelEncoder()
wine['quality'] = label_quality.fit_transform(wine['quality'])
#print(wine['quality'].value_counts())


#plt.show(sns.countplot(wine['quality']))
x = wine.drop('quality',axis = 1)
y = wine['quality']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#RANDOM FOREST CLASSIFIER

rfc = RandomForestClassifier(n_estimators=200)#how many trees in forest
rfc.fit(x_train,y_train)
pred_rfc = rfc.predict(x_test)

#print(classification_report(y_test,pred_rfc))

#SVM CLASSIFIER
clf = svm.SVC()
clf.fit(x_train,y_train)
pred_clf = clf.predict(x_test)

#print(classification_report(y_test,pred_clf))
#print(confusion_matrix(y_test,pred_clf))

#neural network

mlpc=MLPClassifier(hidden_layer_sizes=(11,11,11),max_iter=500)
mlpc.fit(x_train,y_train)
pred_mlpc = mlpc.predict(x_test)

#print(classification_report(y_test,pred_mlpc))
#print(confusion_matrix(y_test,pred_mlpc))





#breast cancer example with random forest

#from sklearn.datasets import load_breast_cancer

#cancer = load_breast_cancer()
#x_train,x_test,y_train,y_test = train_test_split(cancer.data,cancer.target,random_state = 0)

#forest = RandomForestClassifier(n_estimators=100, random_state = 0)
#forest.fit(x_train,y_train)
#print('accuracy on the test subset: {:.3f}'.format(forest.score(x_test,y_test)))
'''

ddos = pd.read_csv("C:\\Users\\Deep\\Desktop\\odl-ddos-detect\\testdataset2.csv")
#x= ddos.drop('Column5',axis = 1)
#y = ddos['Column5']
x = ddos.drop('Column5',axis = 1)
y = ddos['Column5']

kmeans = KMeans(n_clusters=2)
KMmodel = kmeans.fit(x)
KMmodel.labels_
KMmodel.cluster_centers_
print(KMmodel.labels_)
print(KMmodel.cluster_centers_)
#testing with a new variable
xnew = [[200,100,20000,40000]]
#xnew = sc.transform(xnew)
ynew = kmeans.predict(xnew)
print(ynew)

print(pd.crosstab(y,KMmodel.labels_))#see how many get labelled as 0 or 1
pca = PCA(n_components=3).fit(x)
pca_3d = pca.transform(x)
for i in range(0,pca_3d.shape[0]):
    if y[i] == 0:
        c1 = pl.scatter(pca_3d[i,0],pca_3d[i,1],pca_3d[i,2],c='r', marker='+')
    elif y[i] == 1:
        c2 = pl.scatter(pca_3d[i,0],pca_3d[i,1],pca_3d[i,2],c='g', marker='o')
pl.legend([c1, c2], ['NOT', 'DDOS'])
pl.title('Iris dataset with 3 clusters and known outcomes')

pl.show()


    
#x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
#sc = StandardScaler()
#x_train = sc.fit_transform(x_train)
#x_test = sc.transform(x_test)

#RANDOM FOREST CLASSIFIER

#rfc = RandomForestClassifier(n_estimators=200)#how many trees in forest
#rfc.fit(x_train,y_train)
#pred_rfc = rfc.predict(x_test)

#print(classification_report(y_test,pred_rfc))
#print('This models accuracy is:')
#print(accuracy_score(y_test,pred_rfc))

#testing with a new variable
#xnew = [[300,700,20000,40000]]
#xnew = sc.transform(xnew)
#ynew = rfc.predict(xnew)
#print(ynew)

#bins = (2,-1,1)
#labels = ['bad','good']
#print(ddos['Column18'].value_counts())
#ddos['Column18'] = pd.cut(ddos['Column18'], bins = bins, labels = labels)
#label_quality = LabelEncoder()
#ddos['Column18'] = label_quality.fit_transform(ddos['Column18'])
#print(ddos['Column18'].value_counts())
