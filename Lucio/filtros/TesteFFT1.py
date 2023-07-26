import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft
from scipy.fftpack import fftfreq



df = pd.read_csv("C:\\Users\\PC_Beebop\\Desktop\\IA\\graficos2\\2022-05-05_14-55-25.csv", sep=';')

df['mean'] = (df['ch0'] + df['ch1'] + df['ch2'] + df['ch3']) / 4

timeMS = 60000

N = np.arange(0,timeMS,1)

channel = 'mean'

########### Separando em Mão aberta e fechada ###########
hand_flex_curl = df.loc[df['gesture'] == 'hand_flex_curl']
hand_flex_curl = hand_flex_curl[channel]
hand_flex_curl = hand_flex_curl.head(timeMS)
# print("da mao fechada")
# print(hand_flex_curl.shape)

hand_open = df.loc[df['gesture'] == 'hand_open']
hand_open = hand_open[channel]
hand_open = hand_open.head(timeMS)
#########################################################


#pegando apenas um canal
df2 = df[channel]
df2 = df2.head(timeMS)
x = df2

sig_fft = fft(x)

sig_fft_filtered = sig_fft.copy()

freq = fftfreq(len(x), d=1./2000)

cut_off = 6

sig_fft_filtered[np.abs(freq) < cut_off] = 0
filtered = ifft(sig_fft_filtered)

# plot the filtered signal
plt.figure(figsize = (12, 6))
plt.plot(N, filtered)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

plt.plot(N,x)
plt.show()

