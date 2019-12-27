# sorteios
import random
# avaliacao de tempo
import datetime
# sleep
import time
# limpar tela
import os

# numero de pais
numeroPais = 4
# inicializa numero de geracao
generation = 0
# define os caracteres possiveis
geneSet="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'-,.@§çÇáÁéÉóÓãÃõÕêÊẽẼíÍ1234567890\n "
# define o objetivo
target="Last things last\nBy the grace of the fire and the flames\nYou're the face of the future\nThe blood in my veins, oh-ooh\nThe blood in my veins, oh-ooh\nBut they never did, ever lived, ebbing and flowing\nInhibited, limited\nTill it broke open and rained down\nAnd rained down, like"
target="baseado"
def touplesSort(e):
  return e[2]

# gera um indivíduo todo " " de tamanho lenght
def generateCleanParent(length): 
    genes = []
    while len(genes) < length:
        genes.extend('m')
    return ''.join(genes)

# gera um indivíduo aleatorio de tamanho lenght
def generateParent(length):
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
def getFitness(guess):
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
def mutate (parent):
    # define aleatoriamente um ponto de mutacao dentro do parent
    index = random.randrange(0, len(parent))
    # cria um filho com os genes do parent
    childGenes = list(parent)
    # cria uma lista com 2 elementos aleatorios (draws diferentes) de geneSet e atribui o primeiro a newGene e o segundo a alternate
    newGene, alternate = random.sample(geneSet,2)
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

def display(guess):
    # calcula tempo atual - tempo de inicio
    timeDiff = datetime.datetime.now() - startTime
    # calcula o fitness do guess
    fitness = getFitness(guess)
    # limpa tela (cls para windows, clear para outros)
    os.system('cls' if os.name == 'nt' else 'clear')
    # imprime no formato "guess numeroDaGeracao"
    print("{0}\t{1}".format(guess, generation))
    # print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

# inicializacao das listas
bestParent = []
child = []
bestFitness = []
childFitness = []
absoluteBestCromossome = 0
absoluteBestFitness = 0

# inicializa o random
random.seed()
# define o startTime com a hora atual
startTime = datetime.datetime.now()
# define os primeiros pais (como um conjunto de genes do mesmo tamanho do alvo, mas todos " ")
for x in range(numeroPais):
    bestParent.append(generateCleanParent(len(target)))
# armazena o fitness dos pais
for x in bestParent:
    bestFitness.append(getFitness(x))

while True:
    # aumenta o contador de geracoes
    generation += 1
    
    # cria um filho a partir de uma mutacao de cada pai
    for x in bestParent:
        child.append(mutate(x))
    # calcula e armazena o fitness do filho
    for x in child:
        childFitness.append(getFitness(x))

    # adiciona os filhos aos pais e o fitness dos pais ao dos filhos
    bestParent.extend(child)
    bestFitness.extend(childFitness)


    bestTouples = []
    lastParent = []
    for thisParent in bestParent:
        thisFitness = getFitness(thisParent)
        if (lastParent != thisParent):
            indice = 0
        else:
            indice += 1
        if thisFitness > absoluteBestFitness:
            absoluteBestFitness = thisFitness
            absoluteBestCromossome = thisParent
        bestTouples.append((thisParent, indice, thisFitness))
        lastParent = thisParent

    bestTouples.sort(key=touplesSort)

    bestParent = []
    bestFitness = []

    for x in range(numeroPais):
        elemento = bestTouples.pop(-1)
        bestParent.append(elemento[0])
        bestFitness.append(elemento[2])
    # time.sleep(.00005)
    # if generation > 5:
    #     break

    # print(str(len(bestParent)))

    # mostra o filho (que nesse ponto ja sabemos que e melhor que o seu pai)
    # display(child)
    # se o fitness do filho for igual ao tamanho do melhor pai 
    #### (nesse caso poderia ser o tamanho do melhor pai, do filho, do target)
    #### encerra o algoritmo, ja que a melhor solucao tem todos os caracteres corretos
    if absoluteBestFitness >= len(target):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(absoluteBestCromossome + " \n" + str(generation) + " geracoes\n" + str(datetime.datetime.now() - startTime))
        return generation
        break
    # caso o melhor fitness nao esteja perfeito, ele e pelo menos melhor que seu pai
    #### portanto sera mantido para a proxima geracao
    #### define o fitness do filho como melhor fitness
    # bestFitness = childFitness
    # e define o filho como melhor solucao
    # bestParent = child



    child = []

    #### rinse and repeat
    #limpe as lista fei