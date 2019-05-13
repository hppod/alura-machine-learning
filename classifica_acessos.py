from sklearn.naive_bayes import MultinomialNB
from dados import carregar_acessos
x, y = carregar_acessos()

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
