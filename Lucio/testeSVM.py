import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np


df = pd.read_csv('C:/Users/PC_Beebop/Desktop/IA/2022-05-05_14-55-25.csv', sep=';')

y = df.drop(columns=['ch0','ch1','ch2','ch3'])

X = df.drop(columns='gesture')

y['gesture'] = y['gesture'].replace('hand_open', 0)

y['gesture'] = y['gesture'].replace('hand_flex_curl', 1)

y = np.ravel(y)

# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=13)

clf = svm.SVC(C=1.0)



clf.fit(X_train,y_train)

print(clf.predict(X_test))

print(clf.score(X_test,y_test))






