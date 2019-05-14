import pandas as pd

df = pd.read_csv('busca.csv')

x = df[['home', 'busca', 'logado']]
y = df['comprou']

print(x)
print(y)