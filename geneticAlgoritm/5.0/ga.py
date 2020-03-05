# sorteios
import random
import numpy as np
import aux
import importer
import sys
import os

melhorFitness = 50000
listabest = []
listafit = []

def gerarSetInicial(cromossomoOriginal, quantidade):
    setCromossomos = []

    tamanhoCromossomo = len(cromossomoOriginal)
    
    for x in range(0, quantidade):
        cromossomo = (list.copy(cromossomoOriginal),np.diag(np.ones(tamanhoCromossomo*2)))
        if random.choice(range(0,5)): #chance de mutacao de 3/4
            nMutacoes = random.choice(range(1,2))# limite de 4 mutacoes
            while nMutacoes > 0:
                cromossomo = mutate(cromossomo)
                nMutacoes-=1
        setCromossomos.append(cromossomo)
    return setCromossomos

def mutate(cromossomoOriginal):
    cromossomo = cromossomoOriginal
    tamanhoCromossomo = len(cromossomo[0])
    registroMutacao = cromossomo[1]
    pontoMutacao = random.choice(range(0,tamanhoCromossomo))
    gene = cromossomo[0][pontoMutacao] #((3, 2), (4, 2))

    genepA = gene[0]  # (3, 2)
    genepB = gene[1]  # (4, 2)

    if genepB[0] == -1: #caso a mutacao seja em um cromossomo "solitario" ela falha
        return cromossomo

    if random.choice([0,1]):
        genepA = (genepA[0], genepA[1] + genepB[1])
        genepB = (genepB[0], 0)
        registroMutacao[pontoMutacao][pontoMutacao] = 0
    else:
        genepB = (genepB[0], genepA[1] + genepB[1])
        genepA = (genepA[0], 0)
        registroMutacao[pontoMutacao+1][pontoMutacao+1] = 0

    gene = (genepA,genepB)
    cromossomo[0][pontoMutacao] = gene
    return cromossomo

def crossover(listaPais):
    cromossomoA, cromossomoB = listaPais[0], listaPais[1]
    tamanhoCromossomo = len(cromossomoA[0])
    # define o ponto aonde os cromossomos vao fazer a troca
    pontoMutacao = random.choice(range(0,tamanhoCromossomo))

    # armazena a lista de mudancas de cada individuo como um array
    registroPA = np.diag(cromossomoA[1])
    registroPB = np.diag(cromossomoB[1])

    # gera um filho com inicio de a e fim de b
    filhoA = cromossomoA[0][:pontoMutacao]
    filhoA.extend(cromossomoB[0][pontoMutacao:])

    # gera um filho com inicio de b e fim de a
    filhoB = cromossomoB[0][:pontoMutacao]
    filhoB.extend(cromossomoA[0][pontoMutacao:])

    # define como par um filho e sua lista de mutacao
    parA = (filhoA, np.diag(registroPA[:pontoMutacao].tolist()+registroPB[pontoMutacao:].tolist()))
    parB = (filhoB, np.diag(registroPB[:pontoMutacao].tolist()+registroPA[pontoMutacao:].tolist()))

    # envia filho a e b para mutacao
    parA = mutate(parA)
    parB = mutate(parB)

    return [parA, parB]

def getIndex1(item):
    return item[1]

def getOrderedPopulacaoFitness(populacao, matrizOriginal, wayFile, numVeiculos):
    populacaoFitness = []
    for x in populacao:
        try:
            populacaoFitness.append((x, fitness(x, matrizOriginal, wayFile, numVeiculos)))

            populacaoFitness = sorted(populacaoFitness, key=getIndex1)
            global listabest
            global listafit
            if populacaoFitness[-1][1] in listafit:
                pass
            else:
                listafit.append(populacaoFitness[-1][1])
                listabest.append(populacaoFitness[-1][0])
        except Exception as e:
            raise e
            print(x)



    return populacaoFitness

def selecaoPais(populacao, matrizOriginal, wayFile, numVeiculos):
    populacaoFitness = getOrderedPopulacaoFitness(populacao, matrizOriginal, wayFile, numVeiculos)

    populacaoFitnessReverso = []
    for x in populacaoFitness:
        fitnessInversoX = populacaoFitness[0][1] / x[1] # melhor (menor) fitness / fitness[x]
        populacaoFitnessReverso.append((x[0], x[1], fitnessInversoX))

    proximaGeracao = []
    while len(proximaGeracao) < len(populacao)/2:
        for x in populacaoFitnessReverso:
            # sorteio = random.uniform(populacaoFitness[0][1], populacaoFitness[-1][1]) #abaixo sugestao para menor elitismo
            sorteio = random.uniform(populacaoFitness[0][1], populacaoFitness[-1][1]+x[1])
            if sorteio > x[1]:
                proximaGeracao.append(x[0])
                if len(proximaGeracao) >= len(populacao)/2:
                    break
    return(proximaGeracao)

def proximaGeracao(populacao, matrizOriginal, wayFile, numVeiculos, solucaoInicial):
    populacaoFitness = getOrderedPopulacaoFitness(populacao, matrizOriginal, wayFile, numVeiculos)
    indice1 = int(len(populacaoFitness)*0.2) # top 20%
    indice2 = int(len(populacaoFitness)*0.8) # top 80%

    t1 = populacaoFitness[:indice1]          # top 20% melhores
    t2 = populacaoFitness[indice1:indice2]   # top 80% melhores - top 20% melhores8
    t3 = populacaoFitness[indice2:]          # top 20% piores

    proximaGeracao = []

    proximaGeracao.append(t1[0][0])
    proximaGeracao.append((solucaoInicial,np.diag(np.ones(len(solucaoInicial)*2))))


    for parcelaPopulacao, probabilidade in zip([t1,t2,t3],[0.75,0.50,0.25]):
        # permanece .75 de t1 , .50 de t2 e .25 de t3
        sobreviventes = []
        tamanhoFinalParcela = len(parcelaPopulacao) * probabilidade
        while len(sobreviventes) < tamanhoFinalParcela:
            for x in parcelaPopulacao:
                if random.choice([0,1]):
                    sobreviventes.append(x[0])
                    if len(sobreviventes) >= tamanhoFinalParcela:
                        break
        proximaGeracao.extend(sobreviventes)
    return proximaGeracao

def fitness(cromossomo, matrizOriginal, wayFile, numVeiculos):
    global melhorFitness

    # print(tamanhoCromossomo)
    tamanhoCromossomo = len(cromossomo[0]*2)
    xd = cromossomo[1]
    sdvec = []
    for i in range(0,tamanhoCromossomo):
        sdi = 0
        if xd[i][i]:
            for j in range(0,tamanhoCromossomo):
                sdi += (matrizOriginal[i][j] * xd[j][j])
        else:
            sdi = 1
        if sdi != 0:
            sdvec.append(1/sdi)
        else:
            sdvec.append(0)
    sd = np.diag(sdvec)

    pcircunflexo = sd.dot(xd.dot(matrizOriginal.dot(xd)))

    try:
        steadyvector = aux.getSteadyVector(pcircunflexo)
        listaDensidades = aux.getDensidade(wayFile, numVeiculos, steadyvector)
    except Exception as e:
        listaDensidades = [sys.maxsize]
        # print (pcircunflexo)
        # raise e

    # lista de densidades do cromossomo
    # fitness e a maior densidade da lista
    fitness = max(listaDensidades)

    return fitness

def resultado(populacao, matrizOriginal, wayFile, numVeiculos):
    best = getOrderedPopulacaoFitness(populacao, matrizOriginal, wayFile, numVeiculos)
    # for x in best:
    #     solucao = np.diag(x[0][1])
    #     densidade = x[1]
    # print(np.diag(best[0][0][1]))
    # print(best[0][1])
    # print(best[0][0][0])

tamanhoPopulacao = 20000
geracoes = 5000
numeroVeiculos = 250


wayfile, matrizOriginal = importer.processInput("wayInfo")
# wayfile, matrizOriginal = importer.processInput("wayInfo")
solucaoInicial = (aux.getCromossomo(wayfile))
populacao = gerarSetInicial(solucaoInicial,tamanhoPopulacao)

originalDensity = fitness((solucaoInicial,np.diag(np.ones(len(solucaoInicial)*2))), matrizOriginal, wayfile, numeroVeiculos)

# sys.exit()

for geracao in range(0,geracoes):
    pais = selecaoPais(populacao, matrizOriginal, wayfile, numeroVeiculos)
    # print('hfon')
    #reproduz
    filhos = []
    for i in range(0, len(pais), 2):
        x = pais[i]
        try:
            y = pais[i+1]
            filhos.extend(crossover([x,y]))
        except Exception as e:
            filhos.append(x)
    populacao = pais
    for x in filhos:
        populacao.append(x)

    populacao = proximaGeracao(populacao, matrizOriginal, wayfile, numeroVeiculos, solucaoInicial)


    if (geracao % 100) == 0:
        print(geracoes-geracao)

# print('best')
# resultado(populacao, matrizOriginal, wayfile, numeroVeiculos)

opora = []
for x,y in zip(listabest, listafit):
    opora.append((np.diag(x[1]), y))

# opora.getOrderedPopulacaoFitness

opora = sorted(opora, key=getIndex1)






os.system('cls' if os.name == 'nt' else 'clear')

print('the original density is ' + str(originalDensity))
print(len(opora))

for x in opora:
    changes = "reversing "
    for y, i in zip(x[0], range(0,len(x[0]))):
        if y == 0:
            changes += str(i+1) + " "
    changes += "the density is " + str(x[1])
    print(changes)