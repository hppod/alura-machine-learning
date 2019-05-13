from sklearn.naive_bayes import MultinomialNB
from dados import carregar_acessos

x, y = carregar_acessos()

treino_dados = x[:90]
treino_marcacoes = y[:90]

teste_dados = x[-9:]
teste_marcacoes = y[-9:]

modelo = MultinomialNB()
modelo.fit(x, y)

resultado = modelo.predict(x)
diferencas = resultado - y
acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(x)
taxa_de_acertos = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acertos)
print(total_de_elementos)
