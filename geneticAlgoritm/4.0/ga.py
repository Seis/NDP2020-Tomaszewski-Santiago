# sorteios
import random
import numpy as np
import aux
import importer

melhorFitness = 50000

def gerarSetInicial(cromossomoOriginal, quantidade):
    setCromossomos = []

    tamanhoCromossomo = len(cromossomoOriginal)
    
    for x in range(0, quantidade):
        cromossomo = (list.copy(cromossomoOriginal),np.diag(np.ones(tamanhoCromossomo*2)))
        if random.choice(range(0,5)): #chance de mutacao de 3/4
            nMutacoes = random.choice(range(4,8))# limite de 4 mutacoes
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
    registroPA = np.diag(cromossomoA[1])
    registroPB = np.diag(cromossomoB[1])

    tamanhoCromossomo = len(cromossomoA[0])
    pontoMutacao = random.choice(range(0,tamanhoCromossomo))
    filhoA = cromossomoA[0][:pontoMutacao]
    filhoA.extend(cromossomoB[0][pontoMutacao:])
    filhoB = cromossomoB[0][:pontoMutacao]
    filhoB.extend(cromossomoA[0][pontoMutacao:])

    registroFA = registroPA[:pontoMutacao].tolist()+registroPB[pontoMutacao:].tolist()
    registroFB = registroPB[:pontoMutacao].tolist()+registroPA[pontoMutacao:].tolist()

    parA = (filhoA, np.diag(registroFA))
    parB = (filhoB, np.diag(registroFB))

    parA = mutate(parA)
    parB = mutate(parB)

    return [parA, parB]

def getIndex1(item):
    return item[1]

def getOrderedPopulacaoFitness(populacao, matrizOriginal, wayFile, numVeiculos):
    populacaoFitness = []
    for x in populacao:
        populacaoFitness.append((x, fitness(x, matrizOriginal, wayFile, numVeiculos)))

    populacaoFitness = sorted(populacaoFitness, key=getIndex1)
    print(populacaoFitness[0][-1])
    print(populacaoFitness[-1][-1])

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

def proximaGeracao(populacao, matrizOriginal, wayFile, numVeiculos):
    populacaoFitness = getOrderedPopulacaoFitness(populacao, matrizOriginal, wayFile, numVeiculos)
    indice1 = int(len(populacaoFitness)*0.2) # top 20%
    indice2 = int(len(populacaoFitness)*0.8) # top 80%

    t1 = populacaoFitness[:indice1]          # top 20% melhores
    t2 = populacaoFitness[indice1:indice2]   # top 80% melhores - top 20% melhores8
    t3 = populacaoFitness[indice2:]          # top 20% piores

    proximaGeracao = []
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

    steadyvector = aux.getSteadyVector(pcircunflexo)

    fitness = max(aux.getDensidade(wayfile, numVeiculos, steadyvector))

    # print(fitness)

    return fitness

def resultado(populacao, matrizOriginal, wayFile, numVeiculos):
    best = getOrderedPopulacaoFitness(populacao, matrizOriginal, wayFile, numVeiculos)
    # for x in best:
    #     solucao = np.diag(x[0][1])
    #     densidade = x[1]
    print(best[0])






tamanhoPopulacao = 100
geracoes = 50
numeroVeiculos = 100

wayfile, pa, matrizOriginal = importer.processInput("wayInfo")
solucaoInicial = (aux.getCromossomo(wayfile))
populacao = gerarSetInicial(solucaoInicial,tamanhoPopulacao)
for geracao in range(0,geracoes):
    pais = selecaoPais(populacao, matrizOriginal, wayfile, numeroVeiculos)

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

    # print(len(filhos))
    # print(len(pais))
    # print(len(populacao))
    # for x in novaPopulacao:

    #     print(x)
    sobreviventes = proximaGeracao(populacao, matrizOriginal, wayfile, numeroVeiculos)

    # print(len(sobreviventes))
    # print(len(populacao))
    # print("---------------------------------------------------------------")
    print(geracao)

resultado(populacao, matrizOriginal, wayfile, numeroVeiculos)
print(melhorFitness)


# numVeiculos = 100

# seti = gerarSetInicial(cs,20)

# teste = (cs, np.diag([1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1]))

# a = fitness(teste, p, wayfile, numVeiculos)

# resultado(seti, p, wayfile, numVeiculos)


# pg = proximaGeracao(seti,pa, wayfile, numVeiculos)
# # print(seti)
# for x in pg:
#     print(x)
# def gerarSetInicial(cromossomoOriginal, quantidade):
# def mutate(cromossomoOriginal):
# def crossover(listaPais):
# def selecaoPais(populacao):
# def proximaGeracao(populacao, matrizOriginal, wayFile, numVeiculos):
# def fitness(cromossomo, matrizOriginal, wayFile, numVeiculos):

# for x in seti:
#     print(x)

# print('----------------------------------------------')

# print(crossover(seti))


# crossover(cs,cs)


# gerarSetInicial(cs,2)






# [((1, 2), (2, 2)), ((3, 2), (4, 2)), ((5, 2), (6, 2)), ((7, 1), (8, 1)), ((9, 1), (10, 1)),
# ((11, 2), (12, 2)), ((13, 2), (14, 2)), ((15, 2), (16, 2))]

