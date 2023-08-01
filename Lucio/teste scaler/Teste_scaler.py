import pandas as pd
from sklearn import preprocessing
from matplotlib import pyplot as plt
import numpy as np


df = pd.read_csv(r'C:\Users\PC_Beebop\Desktop\NN_Myograph\Lucio\teste_scaler\dataset.csv', sep=';')

print(df)

x = df[['ch0','ch1','ch2']]

colors = {"hand_open":"orange", "hand_flex_curl":"blue"}

def selectColor(x){
    if x 
}


# x = df[['gesture','ch0']]


print(x)

scaler = preprocessing.RobustScaler()
X_scaled = scaler.fit_transform(x)
print(X_scaled)

X_scaled_01 = preprocessing.MinMaxScaler()
X_scaled_01 = X_scaled_01.fit_transform(X_scaled)


print('apenas o canal zero')
channel = X_scaled_01[:,0]
print(channel)

time = list(range(120096))

time = np.array(time)

print(time)

plt.plot(time,channel)
plt.show()
