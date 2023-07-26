import numpy as np
import pandas as pd

import scipy
import matplotlib.pyplot as plt
from pylab import rcParams
import urllib
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from sklearn import metrics

address = 'C:/Users/PC_Beebop/Desktop/IA/2022-05-05_14-55-25.csv'

df = pd.read_csv(address, sep=';')

y = df.drop(columns=['ch0','ch1','ch2','ch3'])

X = df.drop(columns='gesture')

y['gesture'] = y['gesture'].replace('hand_open', 0)

y['gesture'] = y['gesture'].replace('hand_flex_curl', 1)

X = preprocessing.scale(X)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=17)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
print(clf)

y_expect = y_test
y_pred = clf.predict(X_test)

print(metrics.classification_report(y_expect, y_pred))

