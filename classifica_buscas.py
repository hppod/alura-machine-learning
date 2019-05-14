from sklearn.naive_bayes import MultinomialNB
import pandas as pd

df = pd.read_csv('busca.csv')

x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

xDummies_df = pd.get_dummies(x_df)
yDummies_df = y_df

x = xDummies_df.values
y = yDummies_df.values

porcentagem_de_treino = 0.9

tamanho_de_treino = int(porcentagem_de_treino * len(y))

treino_dados = x[:tamanho_de_treino]
treino_marcacoes = y[:tamanho_de_treino]

tamanho_de_teste = len(y) - tamanho_de_treino

teste_dados = x[-tamanho_de_teste:]
teste_marcacoes = y[-tamanho_de_teste:]

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acerto)
print(total_de_elementos)
