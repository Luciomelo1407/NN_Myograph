import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("C:\\Users\\PC_Beebop\\Desktop\\IA\\graficos2\\2022-05-05_14-55-25.csv", sep=';')

df['mean'] = (df['ch0'] + df['ch1'] + df['ch2'] + df['ch3']) / 4

timeMS = 60000

x = np.arange(0,timeMS,1)

channel = 'ch0'


hand_flex_curl = df.loc[df['gesture'] == 'hand_flex_curl']
hand_flex_curl = hand_flex_curl[channel]
hand_flex_curl = hand_flex_curl.head(timeMS)


hand_open = df.loc[df['gesture'] == 'hand_open']
hand_open = hand_open[channel]
hand_open = hand_open.head(timeMS)




# print(hand_open)

fig, ax= plt.subplots()

ax.scatter(x,hand_open, c='red')
ax.scatter(x,hand_flex_curl, c='blue')

plt.show()


