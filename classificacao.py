# definindo o primeiro porco. Um array de carcteristicas do porco
# seis elementos que conhecemos
# 3 variaveis -> é gordinho? tem perna curta? faz au au?

porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

# definindo o array de varios dados
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# +1 para dizer que é porco e -1 para dizer que é cachorro
marcacoes = [1, 1, 1, -1, -1, -1]

# elemento misterioso, será que ele é cachorro ou porco?
misterioso = [1, 1, 1]

# importando o algoritmo de treinamenot
from sklearn.naive_bayes import MultinomialNB