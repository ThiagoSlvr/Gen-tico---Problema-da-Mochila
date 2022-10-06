from func import *

# Inicialização das variaveis
# itens = [(peso, valor), ... ]
# itens = [(12,4),(1,2),(2,2),(1,1),(4,10)]
itens =  [(10,10), (5,5), (1,1), (5,2), (9,7)]
carga_maxima_mochila = 15
tamanho_populacao = 10
epocas = 300
 
# Chamada da função populacao no codigo func.py
# def populacao: cria primeira populaçao, sendo aleatoria
pop = populacao(tamanho_populacao, len(itens))
# print('População: '+str(pop))

# Chamada da função calculo_fitness no codigo func.py
# def calculo_fitness: calcula o fitnes de cada individuo, retornando:
# [[peso total do individuo, preço total do individuo,[individuo]],...]
calculo_fitness = [fitness(pop[x], itens) for x in range(tamanho_populacao)]
# print("Calculo fitness: "+str(calculo_fitness))

# Inicalização do contador para epocas
cont_epoca = 0

# Loop principal para geração de novas populações durante o periodo definido
while cont_epoca !=epocas:
    print(calculo_fitness)
    nova_pop = evolucao(calculo_fitness, carga_maxima_mochila, tamanho_populacao)
    calculo_fitness = [fitness(nova_pop[x], itens) for x in range(tamanho_populacao)]
    cont_epoca+=1