import re
import numpy as np

file = open("output", "r")
lines = file.readlines()
filesize = len(lines)
indexIdList = [] # (index, id)
idIndexList = [] # (id, index)
wayFile = []

#gera waylist com info do arquivo, gera tambem indexid e idindex, adiciona o comprimento normalizado
def fileProcess():
    global indexIdList
    global idIndexList
    global wayFile

    for x in range(0,filesize,5):
        wayId = lines[x]
        wayLen = lines[x+1]
        waylane = lines[x+2]
        wayOpossite = lines[x+3]
        wayProb = lines[x+4]

        wayId = int(re.sub("\n",'',wayId))
        wayLen = float(re.sub("\n",'',wayLen))
        wayOpossite = int(re.sub("\n",'',wayOpossite))
        waylane = int(re.sub("\n",'',waylane))

        wayProb = re.sub("\n",'',wayProb)

        wayProb = wayProb.split('|')
        probs = []
        for x in range(0,len(wayProb),2):
            probs.append((int(wayProb[x]),float(wayProb[x+1])))

        way = [wayId, wayLen, waylane, probs, wayOpossite]
        wayFile.append(way)
    wayFile = sorted(wayFile, key=getFirstAsKey)

    for x in range(0,len(wayFile)):
        indexIdList.append((x,wayFile[x][0]))
        idIndexList.append((wayFile[x][0],x))

    idIndexList = dict(idIndexList)

    return wayFile

def getCromossomo(waylist):
    cromossomo = []
    wayId = []
    wayLanes =[]
    wayOpossite = []
    wayPresent = []
    for way in waylist:
        wayId.append(way[0])
        wayLanes.append(way[2])
        wayOpossite.append(way[4])
        wayPresent.append(False)
    for x in zip():
        pass
    return length, lanes





def getLengthLanes(waylist):
    length = []
    lanes = []
    for x in waylist:
        length.append(x[1])
        lanes.append(x[2])
    return length, lanes

def getFirstAsKey(item):
    return item[0]

def indexToId(index):
    wayId = indexIdList[index][1]
    return wayId

def idToIndex(wayId):
    wayIndex = idIndexList[wayId]
    return wayIndex

def getTransitionMatrix():
    transitionProbability = np.zeros(shape=(len(wayFile),len(wayFile)))
    for wayFrom in range(0,len(wayFile)):
        for wayTo in wayFile[wayFrom][3]:
            transitionProbability[wayFrom][idToIndex(wayTo[0])] = wayTo[1]

    return transitionProbability

def calculeAutoLoop():
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

def insertAutoLoop(transitionProbability):
    transitionProbabilityAuto = np.matrix.copy(transitionProbability)
    autoloop = calculeAutoLoop()

    for x in range(0,len(wayFile)):
        for y in range(0,len(wayFile)):
            if x != y:
                transitionProbabilityAuto[x][y] = (1-autoloop[x])*transitionProbabilityAuto[x][y]
            else:
                transitionProbabilityAuto[x][y] = autoloop[x]
    return transitionProbabilityAuto

def processInput():
    wayFile = fileProcess()
    pAccent = getTransitionMatrix()
    P = insertAutoLoop(pAccent)

    wayInfos = []

    #id comprimento e num lanes
    for x in wayFile:
        wayInfos.append([x[0],x[1],x[2]])


    return wayInfos, pAccent, P