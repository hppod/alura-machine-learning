import pandas as pd

df = pd.read_csv('busca.csv')

x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

xDummies_df = pd.get_dummies(x_df)
yDummies_df = y_df

x = xDummies_df.values
y = yDummies_df.values

