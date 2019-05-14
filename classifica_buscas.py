import pandas as pd

df = pd.read_csv('busca.csv')

x = df[['home', 'busca', 'logado']]
y = df['comprou']

xDummies = pd.get_dummies(x)
yDummies = pd.get_dummies(y)

print(xDummies)
