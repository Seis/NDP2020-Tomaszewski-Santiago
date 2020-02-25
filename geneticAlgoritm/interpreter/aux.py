import numpy as np

def getSteadyVector(p):
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
    indexIdList = []
    idIndexList = []

    usedWays = []


    for x in range(0,len(waylist)):
        indexIdList.append((x,waylist[x][0]))
        idIndexList.append((waylist[x][0],x))
    idIndexList = dict(idIndexList)

    for way in waylist:
        if way[0] in usedWays: #via ja apareceu no cromossomo?
            pass
        else:
            #extrai o cromossomo
            # print(way)
            geneA = (way[0],way[2])
            geneB = (way[3],waylist[idIndexList[way[3]]][2]) 
            gene = (geneA,geneB)
            # indexGeneB = idIndexList[way[3]]
            # print(waylist[idIndexList[way[3]]][2])
            usedWays.append(way[0])
            usedWays.append(way[3])
            cromossomo.append(gene)
            # way.append(True)
    return cromossomo












# def indexToId(index, indexIdList):
#     wayId = indexIdList[index][1]
#     return wayId

# def idToIndex(wayId, idIndexList):
#     wayIndex = idIndexList[wayId]
#     return wayIndex