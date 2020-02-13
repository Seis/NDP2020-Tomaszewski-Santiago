# coding: utf8

import sys
# sorteios
import random
# avaliacao de tempo
import datetime
# sleep
import time
# limpar tela
import os

# gera um indivíduo todo char de tamanho lenght
def generateStandartParent(length, char): 
    genes = []
    while len(genes) < length:
        genes.extend(char)
    return ''.join(genes)

# gera um indivíduo aleatorio de tamanho lenght
def generateParent(length, geneSet):
    # define os genes de um pai como vazio
    genes = []
    # ocorre o numero necessario de vezes para que o pai tenha lenght genes
    while len(genes) < length:
        # define o tamanho da amostra como o minimo entre o numero de genes que faltam e o numero de genes diponiveis na pool
        sampleSize = min(length - len(genes), len(geneSet))
        # estende a lista de genes do pai com a quantidade definida acima, com elementos tirados aleatoriamente do geneSet
        genes.extend(random.sample(geneSet, sampleSize))
    #retorna genes como uma string
    return ''.join(genes)

# retorna o numero de caracteres certos em guess comparado a target
def getFitness(guess,target):
    # caracteres corretos
    correct = 0
    # gera uma tupla com (expected, atual) para cada entrada em (target, guess) e percorre todas as tuplas
    for (expected,atual) in zip(target, guess):
        # soma para cada correto
        if expected == atual:
            correct += 1
    # retorna numero de acertos
    return correct

# cria uma mutacao de um cromossomo em parent a partir de um ponto aleatorio
def mutate (parent, geneSet):
    # define aleatoriamente um ponto de mutacao dentro do parent
    index = random.randrange(0, len(parent))
    # cria um filho com os genes do parent
    childGenes = list(parent)
    # cria uma lista com 2 elementos aleatorios (draws diferentes) de geneSet e atribui o primeiro a newGene e o segundo a alternate
    newGene, alternate = random.sample(geneSet,2)
    # newGene = random.sample(getGeneSet(), 1)
    # alternate = random.sample(getGeneSet(), 1)
    # se o gene atual for igual a mutacao sorteada, usa o sorteio alternativo
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    # <codigo equivalente ao acima> nao condensado
    # if childGenes[index] != newGene:
    #     childFitness[index] = newGene
    # else
    #     childFitness[index] = alternate
    # <!codigo equivalente ao acima>

    # retorna genes como uma string
    return ''.join(childGenes)

def display(guess, startTime, generation):
    # calcula tempo atual - tempo de inicio
    timeDiff = datetime.datetime.now() - startTime
    # limpa tela (cls para windows, clear para outros)
    os.system('cls' if os.name == 'nt' else 'clear')
    # imprime no formato "guess numeroDaGeracao"
    print("{0}\n{1} generations".format(guess[0], generation))
    # print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

def crossoverMutacaoSimples(listaTuplasPais, geneSet, target):
    # crossover mutacao obrigatoria em todos
    # retorna lista com 1 filho mutado de cada 
    childsTuplesList = []
    for parent in listaTuplasPais:
            # cria um filho a partir de uma mutacao em cada pai
            child = mutate(parent[0], geneSet)
            # calcula e armazena o fitness do filho
            childFitness = getFitness(child, target)
            childsTuplesList.append((child, childFitness))
    return childsTuplesList

def getKeyFitness(item):
    return item[1]

def nextGeneration(listaTuplas):
    # retorna os top 50%
    listaTuplas = sorted(listaTuplas, key=getKeyFitness)
    newGeneration = []
    for x in listaTuplas[(len(listaTuplas)/2):]:
        newGeneration.append(x)


    return newGeneration
def inicialize(geneSet, generation, target, ancestrais):
    # inicializa o random
    random.seed()
    # define o startTime com a hora atual
    startTime = datetime.datetime.now()

    fitnessMax = len(target)

    bestFitness = 0
    bestParent = ''
    parentsTuplesList = []

    # armazena o fitness dos pais

    if len(target) < ancestrais:
        pass
    for parent in ancestrais:
        fitnessAncestral = getFitness(parent, target)
        pai = (parent, fitnessAncestral)
        parentsTuplesList.append(pai)
        # define o primeiro melhor pai (como um conjunto de genes do mesmo tamanho do alvo, mas todos " ")
        if fitnessAncestral > bestParent:
            bestParent = parent
            bestFitness = parentsFitness[-1]

    # mostra o fitness do melhor pai
    # display(bestParent, startTime, generation)






    while bestFitness < fitnessMax:
        # crossover (gera uma lista de filhos com uma mutacao)
        childsTuplesList = crossoverMutacaoSimples(parentsTuplesList, geneSet, target)
        # junta pais aos filhos
        parentsTuplesList.extend(childsTuplesList)
        # selecao de pais
        parentsTuplesList = nextGeneration(parentsTuplesList)

        # aumenta o contador de geracoes
        generation += 1

        # time.sleep(0.005)

        display(parentsTuplesList[-1], startTime, generation)
        # if generation%100 == 0:
        #     os.system('cls' if os.name == 'nt' else 'clear')
        #     print(generation)
        



        bestFitness = parentsTuplesList[-1][1]

        #### rinse and repeat
    display(parentsTuplesList[-1], startTime, generation)

    return generation
