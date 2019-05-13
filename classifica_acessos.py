from sklearn.naive_bayes import MultinomialNB
from dados import carregar_acessos
x, y = carregar_acessos()

modelo = MultinomialNB()
modelo.fit(x, y)
