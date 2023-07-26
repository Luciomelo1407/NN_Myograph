from sklearn.neighbors import (NeighborhoodComponentsAnalysis, KNeighborsClassifier)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np

address = 'C:/Users/PC_Beebop/Desktop/IA/2022-05-05_14-55-25.csv'

df = pd.read_csv(address, sep=';')

y = df.drop(columns=['ch0','ch1','ch2','ch3'])

X = df.drop(columns='gesture')

y['gesture'] = y['gesture'].replace('hand_open', 0)

y['gesture'] = y['gesture'].replace('hand_flex_curl', 1)

y = np.ravel(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.7, random_state=42)

nca = NeighborhoodComponentsAnalysis(random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)

nca_pipe = Pipeline([('nca', nca), ('knn', knn)])

nca_pipe.fit(X_train, y_train)

print(nca_pipe.score(X_test, y_test))
