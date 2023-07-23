import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

base = pd.read_csv(r'C:\Users\PC_Beebop\Desktop\IA\testes\2022-05-05_14-55-25.csv', sep=';')


X = base.drop('gesture', axis=1).values
y = base['gesture'].values

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)



scaler_x = StandardScaler()
X = scaler_x.fit_transform(X)


X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.3)

classificador = LogisticRegression(max_iter = 1000000)
classificador.fit(X_treinamento, y_treinamento)

previsoes = classificador.predict(X_teste)

taxa_acerto = accuracy_score(y_teste, previsoes)
print(taxa_acerto)

# accuracy = 0.4913819423242388
'''
    Num funcionou nn man sinto mto
    
'''