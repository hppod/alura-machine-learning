import pandas as pd

df = pd.read_csv('busca.csv')

x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

xDummies_df = pd.get_dummies(x_df)
yDummies_df = y_df

x = xDummies_df.values
y = yDummies_df.values

tamanho_de_treino = 0.9 * len(y)

treino_dados = x[:tamanho_de_treino]
treino_marcacoes = y[:tamanho_de_treino]

tamanho_de_teste = len(y) - tamanho_de_treino

teste_dados = x[-tamanho_de_teste:]
teste_marcacoes = y[-tamanho_de_teste:]
