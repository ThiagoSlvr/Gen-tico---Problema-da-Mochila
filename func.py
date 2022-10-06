from math import floor
from random import randint, random
from operator import add, itemgetter
from functools import reduce

#cria os primeiros individuos, sendo completamente aleatorio
def individuo(itens):
    return [randint(0, 1) for x in range(itens)]

#cria primeira populaçao, sendo aleatoria
def populacao(tamanho_populacao, itens):
    return [individuo(itens) for x in range(tamanho_populacao)]

#calcula o fitness de cada individuo, retornando:
#[[peso total do individuo, preço total do individuo,[individuo]],...]
def fitness(pop, itens):
    fit = [[pop[x]*itens[x][0], pop[x]*itens[x][1]] for x in range(len(itens))]
    return [reduce(add, map(itemgetter(0), fit), 0), reduce(add, map(itemgetter(1), fit), 0), pop]

#função de evoluçao
def evolucao(pop, carga_maxima_mochila, tamanho_populacao, mutacao = 0.25):

    #variavel utilizada apenas quando se utiliza roleta onde nao permite pai=mae
    acima_carga_maxima = None
    
    #organiza lista com base no peso
    pop.sort()
    
    #exclui soluções que tenham mais peso do que a carga maxima da mochila
    for x in pop:
        if x[0] > carga_maxima_mochila:
            acima_carga_maxima = pop.index(x)
            break

    pais = pop[:acima_carga_maxima]

    #cria nova lista apenas com preço e individuo
    pais = [[x[1], x[2]]for x in pais]

    #organiza com base nos preços
    pais.sort()

    #soma dos preços dos individuos
    valor_absoluto = reduce(add, map(itemgetter(0), pais), 0)

    #loop para criar nova pupulação ate que nova_pop seja igual ao tamanho da população pre definida
    #seleciona um pai e uma mae e cria dois filhos
    nova_pop = []
    while len(nova_pop) -1 < tamanho_populacao:
        pai = roleta(pais, valor_absoluto)
        mae = roleta(pais, valor_absoluto)
        #caso queira utilizar roleta com pai != mae
        #mae = roleta(pais, valor_absoluto, pai)
        filho = cria_filho(pai[1], mae[1])
        nova_pop.extend(filho)

    #caso seja maior que o previsto
    if len(nova_pop) > tamanho_populacao:
        nova_pop.pop()

    #chance de mutação, muda apenas um gene aleatorio
    for x in nova_pop:
        if random() < mutacao:
            gene = randint(0, len(x)-1)
            x[gene] = 0 if x[gene] == 1 else 1

    return nova_pop

#funçao para criar dois filho um com metada inicial do pai e final da mae e o outro o oposto
def cria_filho(pai, mae):
    corte = floor(len(pai)/2)
    return [pai[:corte] + mae[corte:], mae[:corte] + pai[corte:]]

# # roleta que impede pai = mae
# def roleta(pop, valor_absoluto, excluido = None):
#     soma=0
#     d=randint(0, valor_absoluto if excluido is None else valor_absoluto - excluido[0])
#     for p in pop:
#         if excluido is None or p!=excluido:
#             soma += p[0]
#             if soma >=d:
#                 return p

# roleta possibilita pai = mae
def roleta(pop, valor_absoluto):
    soma=0
    d=randint(0, valor_absoluto)
    for p in pop:
        soma += p[0]
        if soma >=d:
            return p
