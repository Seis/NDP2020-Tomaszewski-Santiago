import numpy as np

# returns the steady state probabilities (pi) for an transition probability matrix
def getSteadyVector(transitionProbabilityMatrix):
    try:
        p = np.matrix(transitionProbabilityMatrix)
        dim = p.shape[0]
        q = (p-np.eye(dim))
        ones = np.ones(dim)
        q = np.c_[q,ones]
        QTQ = np.dot(q, q.T)
        bQT = np.ones(dim)
        vector = np.linalg.solve(QTQ,bQT)
    except Exception as e:
        raise e
    return vector

# normalize the lengths of the road network, then returns the auto loop probability
def lengthNormalization(lengthList):
    # lengths are extracted from wayFile second column
    

    minimumLength = min(lengthList)
    normalizedLengths = []
    for way in lengthList:
        normalizedLengths.append(way/minimumLength)

    autoloop = []
    for normalizedWay in normalizedLengths:
        autoloop.append((normalizedWay-1)/normalizedWay)
    return autoloop

# modifies a transition probability matrix to accounts the auto-loop chance
def insertAutoLoop(transitionProbability,wayFile):
    transitionProbabilityAuto = np.matrix.copy(transitionProbability)
    
    # lengths are extracted from wayFile second column
    autoloop = lengthNormalization(np.matrix(wayFile)[:,1])

    for x in range(0,len(wayFile)):
        for y in range(0,len(wayFile)):
            if x != y:
                transitionProbabilityAuto[x][y] = (1-autoloop[x])*transitionProbabilityAuto[x][y]
            else:
                transitionProbabilityAuto[x][y] = autoloop[x]
    return transitionProbabilityAuto

# read a list with the road network info, then return a list of road tuples of roads
# in format ((road1, numWays),(opossiteToRoad1, numWays))
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
    return cromossomo

# returns 2 lists with the length and the lane number of a road network respectively 
def getLengthLanes(waylist):
    length = []
    lanes = []
    for x in waylist:
        length.append(x[1])
        lanes.append(x[2])
    return length, lanes

# returns the density of a road network for a certain steady chance
def getDensidade(wayfile, numVeiculos, steadyChance):
    densidade = []

    length, lanes = getLengthLanes(wayfile)
       
    for (lengthIndividual, laneIndividual , pii) in zip(length, lanes, steadyChance):
        densidadeIndividual = 0
        divisor = laneIndividual*lengthIndividual
        if divisor != 0:
            densidade.append((numVeiculos*pii)/divisor)
        else:
            densidade.append(0)

    return densidade
