import re
import numpy as np

file = open("output", "r")
lines = file.readlines()
filesize = len(lines)

def getFirstAsKey(item):
    return item[0]


wayFile = []

for x in range(0,filesize,4):
    wayId = lines[x]
    wayLen = lines[x+1]
    waylane = lines[x+2]
    wayProb = lines[x+3]

    wayId = re.sub("\n",'',wayId)
    wayLen = float(re.sub("\n",'',wayLen))
    waylane = int(re.sub("\n",'',waylane))

    wayProb = re.sub("\n",'',wayProb)

    wayProb = wayProb.split('|')
    probs = []
    for x in range(0,len(wayProb),2):
        probs.append((int(wayProb[x]),float(wayProb[x+1])))

    way = [wayId, wayLen, waylane, probs]
    wayFile.append(way)



idList = []
for x in wayFile:
    idList.append(x[0])

lengthList = []
for x in wayFile:
    lengthList.append(x[1])

minimumLength = min(lengthList)
for x in wayFile:
    x[1] = x[1]/minimumLength


vetor de tamanho normalizado, falta arrumar a matriz de prob































































# idList = []
# for x in range(0, len(info)):
#     idList.append((x,int(info[x][0])))

# # for x in idList:
#     # print(info[x[1]])
# idList = sorted(idList, key=getFirstAsKey)

# matrizP = []
# idList = dict(idList)

# print(idList)
# print()
# print()
# print()
# print()
# # idList  [0] wayid from info
# #         [1] index from info

# minlane = 1
# maxlane = 6
# matrizProbabilidade = np.zeros((len(idList),len(idList)))


# for laneFrom in range(0,len(idList)):

#     arrayTo = info[laneFrom][3]
#     print(arrayTo)
#     arrayTo = dict(arrayTo)
#     for laneTo in range(0,len(idList)):
#         try:
#             print(idList.get(laneTo))
#             print(arrayTo[str(laneTo)])
#         except Exception as e:
#             print(0)
#     print()

#     break


    # print(info[laneFrom][3])
    # tempwayid =idList[laneFrom][0]
    # tempinfoindex = idList[laneFrom][1]
    # print(info(tempinfoindex))
    # print(tempwayid)
    # print(matrizProbabilidade[laneFrom])











# for laneFrom[] in idList:
#     print(laneFrom)
#     for laneTo in matrizProbabilidade[int(laneFrom)]:
#         print(info[idList[laneFrom]][3])

    # for laneTo in info[idList[laneFrom]][3]:

        
    #     print(str(laneFrom) + " - " + str(laneTo))










# 2
# 150
# 2
# 1|0.1|4|0.3|8|0.3
# 1
# 150
# 2
# 2|0.1|6|0.9