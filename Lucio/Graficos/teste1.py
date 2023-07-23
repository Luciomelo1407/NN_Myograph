import matplotlib as mp
from matplotlib import pyplot as plt
import pandas as pd

address = 'C:/Users/PC_Beebop/Desktop/IA/Graficos/DatasetTime.csv'

df = pd.read_csv(address)

chUsed = 'ch0'

df['mean'] = (df['ch0'] + df['ch1'] + df['ch2'] + df['ch3']) / 4

hand_open = df.copy()
hand_open.loc[hand_open['gesture'] == 'hand_flex_curl', chUsed] = 0

hand_close = df.copy()
hand_close.loc[hand_close['gesture'] == 'hand_open', chUsed] = 0

x = df['time']

y1 = hand_open[chUsed]

y2 = hand_close[chUsed]

plt.plot(x,y1)
plt.plot(x,y2)
plt.xlim(0,2089)
plt.ylim(1500,3000)



plt.show()

#ate 2089