import re
import numpy as np
import aux as a

indexIdList = [] # (index, id)
idIndexList = [] # (id, index)

#gera waylist com info do arquivo, gera tambem indexid e idindex, adiciona o comprimento normalizado
#gera lista de ruas, cada rua e uma lista
#composta por id, comprimento, numero de vias, probabilidades de conversao e id de sua via oposta
#prob de conversao sao representadas como uma lista de tuplas com cada tupla sendo id destino, probabilidade

def fileProcess(fileToProcess):
    global indexIdList
    global idIndexList
    wayFile = []

    file = open(fileToProcess, "r")
    lines = file.readlines()
    filesize = len(lines)

    for x in range(0,filesize,5):
        wayId = lines[x]
        wayLen = lines[x+1]
        waylane = lines[x+2]
        wayOpossite = lines[x+3]
        wayProb = lines[x+4]

        wayId = int(re.sub("\n",'',wayId))
        wayLen = float(re.sub("\n",'',wayLen))
        wayOpossite = stringCut(wayOpossite,int)
        # wayOpossite = int(re.sub("\n",'',wayOpossite))
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

def stringCut(input, param):
    try:
        retorno = re.sub("\n",'',input)
        if param == int:
            retorno = int(retorno)
    except Exception as e:
        return -1
    return retorno
    pass

def getFirstAsKey(item):
    return item[0]

def indexToId(index):
    wayId = indexIdList[index][1]
    return wayId

def idToIndex(wayId):
    wayIndex = idIndexList[wayId]
    return wayIndex

def getTransitionMatrix(wayFile):
    transitionProbability = np.zeros(shape=(len(wayFile),len(wayFile)))
    for wayFrom in range(0,len(wayFile)):
        for wayTo in wayFile[wayFrom][3]:
            transitionProbability[wayFrom][idToIndex(wayTo[0])] = wayTo[1]

    return transitionProbability

def processInput(fileToProcess):
    wayFile = fileProcess(fileToProcess)
    pAccent = getTransitionMatrix(wayFile)
    P = a.insertAutoLoop(pAccent,wayFile)

    #id comprimento  num lanes e via oposta
    wayInfos = []
    for x in wayFile:
        wayInfos.append([x[0],x[1],x[2],x[4]])

    return wayInfos, pAccent, P