import matplotlib as mp
from matplotlib import pyplot as plt
import pandas as pd

address = 'C:/Users/PC_Beebop/Desktop/IA/Graficos/DatasetTime2.csv'

address2 = 'C:/Users/PC_Beebop/Desktop/IA/Graficos/DatasetTime_hand_open.csv'

address3 = 'C:/Users/PC_Beebop/Desktop/IA/Graficos/DatasetTime_hand_flex_curl.csv'



df = pd.read_csv(address)

chUsed = 'mean'

print(df)

df['mean'] = (df['ch0'] + df['ch1'] + df['ch2'] + df['ch3']) / 4

# hand_open = df.copy()
# hand_open.loc[hand_open['gesture'] == 'hand_flex_curl', chUsed] = 0

hand_open = df.loc[df['gesture'] == 'hand_open']


hand_open.to_csv(address2, index=False);

print(hand_open)


# hand_close.loc[hand_close['gesture'] == 'hand_flex_curl', chUsed] = 0


hand_flex_curl = df.loc[df['gesture'] == 'hand_flex_curl']

hand_flex_curl = hand_flex_curl.drop('time',axis=1)

hand_flex_curl.to_csv(address3, index=True);

print(hand_flex_curl)