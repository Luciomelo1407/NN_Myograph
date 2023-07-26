import pandas as pd
import matplotlib 
from matplotlib import pyplot as plt

channel = 'ch0'

address = 'C:/Users/PC_Beebop/Desktop/IA/2022-05-05_14-55-25.csv'

df = pd.read_csv(r'C:\Users\PC_Beebop\Desktop\IA\testes\2022-05-05_14-55-25.csv', sep=';')

y = df['gesture']

x = df.drop('gesture', axis=1)
x = x[channel]

print(x.head())

plt.plot(x,y, 'o')
plt.xlim(2100,2120)

plt.show()