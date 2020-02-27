import numpy as np

def getSteadyVector(p):
    # return V for v.p = v
    dim = p.shape[0]
    q = (p-np.eye(dim))
    ones = np.ones(dim)
    q = np.c_[q,ones]
    QTQ = np.dot(q, q.T)
    bQT = np.ones(dim)
    vector = np.linalg.solve(QTQ,bQT)
    return vector

def calculeAutoLoop(wayFile):
    lengthList = []
    for x in wayFile:
        lengthList.append(x[1])

    minimumLength = min(lengthList)
    tt = [] #normalizedLengths
    for x in wayFile:
        tt.append(x[1]/minimumLength)

    autoloop = []
    for x in tt:
        autoloop.append((x-1)/x)
    return autoloop

def insertAutoLoop(transitionProbability,wayFile):
    transitionProbabilityAuto = np.matrix.copy(transitionProbability)
    autoloop = calculeAutoLoop(wayFile)

    for x in range(0,len(wayFile)):
        for y in range(0,len(wayFile)):
            if x != y:
                transitionProbabilityAuto[x][y] = (1-autoloop[x])*transitionProbabilityAuto[x][y]
            else:
                transitionProbabilityAuto[x][y] = autoloop[x]
    return transitionProbabilityAuto

def getCromossomo(waylist):
    cromossomo = []
    idIndexList = []
    usedWays = []

    for x in range(0,len(waylist)):
        idIndexList.append((waylist[x][0],x))
    idIndexList = dict(idIndexList)

    for way in waylist:
        if way[0] in usedWays: #via ja apareceu no cromossomo?
            pass
        else:
            #extrai o cromossomo
            # print(way)
            try:
                geneA = (way[0],way[2])
                geneB = (way[3],waylist[idIndexList[way[3]]][2]) 
            except Exception as e:
                # define -1 como oposto de vias mao unica
                geneB = (-1,0)

            gene = (geneA,geneB)
            usedWays.append(way[0])
            usedWays.append(way[3])
            cromossomo.append(gene)
            # way.append(True)
    return cromossomo


def getLengthLanes(waylist):
    length = []
    lanes = []
    for x in waylist:
        length.append(x[1])
        lanes.append(x[2])
    return length, lanes


def getDensidade(wayfile, numVeiculos, probEstatica):
    densidade = []

    length, lanes = getLengthLanes(wayfile)
       
    for (lengthIndividual, laneIndividual , pii) in zip(length, lanes, probEstatica):
        try:
            densidade.append((numVeiculos*pii)/(laneIndividual*lengthIndividual))
        except Exception as e:
            densidade.append(0)

    return densidade

def fitness(cromossomo, matrizOriginal, wayfile, numVeiculos):
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
        sdvec.append(1/sdi)
    sd = np.diag(sdvec)

    pcircunflexo = sd.dot(xd.dot(matrizOriginal.dot(xd)))

    steadyvector = getSteadyVector(pcircunflexo)
    densidade = getDensidade(wayfile, numVeiculos, steadyvector)

    fitness = max(densidade)

    # return dumbFitness()
    return fitness


    # 1,1,1,10,1,3.33,1,1,3.33,1,1,1,1,1,1,1  