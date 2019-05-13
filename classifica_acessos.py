from dados import carregar_acessos
x, y = carregar_acessos()

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(x,y)
