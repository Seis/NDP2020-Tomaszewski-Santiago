# sorteios
import random

def gerarSetInicial(cromossomoOriginal, quantidade):
    setCromossomos = []
    for x in range(0, quantidade):
        cromossomo = list.copy(cromossomoOriginal)
        if random.choice(range(0,5)): #chance de mutacao de 3/4
            nMutacoes = random.choice(range(1,4))# limite de 4 mutacoes
            while nMutacoes > 0:
                cromossomo = mutate(cromossomo)
                nMutacoes-=1
        setCromossomos.append(cromossomo)
    return setCromossomos

def mutate(cromossomoOriginal):
    cromossomo = list.copy(cromossomoOriginal)
    tamanhoCromossomo = len(cromossomo)
    pontoMutacao = random.choice(range(0,tamanhoCromossomo))
    gene = cromossomo[pontoMutacao] #((3, 2), (4, 2))

    genepA = gene[0]  # (3, 2)
    genepB = gene[1]  # (4, 2)

    if genepB[0] == -1: #caso a mutacao seja em um cromossomo "solitario" ela falha
        return cromossomo


    if random.choice([0,1]):
        genepA = (genepA[0], genepA[1] + genepB[1])
        genepB = (genepB[0], 0)
    else:
        genepB = (genepB[0], genepA[1] + genepB[1])
        genepA = (genepA[0], 0)

    gene = (genepA,genepB)
    cromossomo[pontoMutacao] = gene
    return cromossomo

def crossover(listaPais):
    cromossomoA, cromossomoB = listaPais[0], listaPais[1]

    tamanhoCromossomo = len(cromossomoA)
    pontoMutacao = random.choice(range(0,tamanhoCromossomo))
    filhoA = cromossomoA[:pontoMutacao]
    for x in cromossomoB[pontoMutacao:]:
        filhoA.append(x)

    filhoB = cromossomoB[:pontoMutacao]
    for x in cromossomoA[pontoMutacao:]:
        filhoB.append(x)

    return filhoA, filhoB

def getIndex1(item):
    return item[1]

def selecaoPais(populacao):
    populacaoFitness = []
    fitnessTotal = 0
    for x in populacao:
        fitnessX = fitness(x)
        fitnessTotal += fitnessX
        populacaoFitness.append((x, fitnessX))

    populacaoFitnessReverso = []

    for x in populacaoFitness:
        fitnessX = x[1]
        fitnessInversoX = fitnessTotal / fitnessX
        populacaoFitnessReverso.append((x, fitnessInversoX))

    populacaoFitnessReverso = sorted(populacaoFitnessReverso, key=getIndex1)


    # wip

    proximaGeracao = []

    while len(proximaGeracao) < len(populacao/2):
        for x in populacao:
            if random.uniform(pais[0], pais[-1]) < x:
                proximaGeracao.append(1)
                print(len(proximaGeracao))
                if len(proximaGeracao) >= len(populacao/2):
                    break
    return(proximaGeracao)





cs = [((1, 2), (2, 2)), ((3, 2), (4, 2)), ((5, 2), (6, 2)), ((7, 1), (8, 1)), ((9, 1), (10, 1)),((11, 2), (12, 2)), ((13, 2), (14, 2)), ((15, 2), (16, 2)), ((17, 1), (-1, 0))]

seti = gerarSetInicial(cs,5)

# for x in seti:
#     print(x)

# print('----------------------------------------------')

print(crossover(seti))


# crossover(cs,cs)


# gerarSetInicial(cs,2)






# [((1, 2), (2, 2)), ((3, 2), (4, 2)), ((5, 2), (6, 2)), ((7, 1), (8, 1)), ((9, 1), (10, 1)),
# ((11, 2), (12, 2)), ((13, 2), (14, 2)), ((15, 2), (16, 2))]

