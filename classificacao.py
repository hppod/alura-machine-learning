# definindo o primeiro porco. Um array de carcteristicas do porco
# seis elementos que conhecemos
# 3 variaveis -> é gordinho? tem perna curta? faz au au?

from sklearn.naive_bayes import MultinomialNB
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
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

# importando o algoritmo de treinamento
modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

testes = [misterioso, misterioso2, misterioso3]

marcacoes_teste = [-1, 1, -1]

resultado = modelo.predict(testes)
print(resultado)

diferencas = (resultado - marcacoes_teste)
print(diferencas)

acertos = [d for d in diferencas if d == 0]
print(acertos)
total_de_acertos = len(acertos)

print(total_de_acertos)
total_de_elementos = len(testes)
print(total_de_elementos)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
print(taxa_de_acerto)

# 1 1 => 1-1=0
# -1 -1 => -1 --1 = -1 + 1 = 0
# -1 1 => -1 -1 = -2
# 1 - 1 => 1 --1 = 1+ 1 = 2
