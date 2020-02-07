import sys
import untangle
arquivo = untangle.parse(str(sys.argv[1]))
#arquivo = untangle.parse("newPonteLenght.osm")
# print("parsing")
waysFile = arquivo.osm.way


wayList = []
incompleteLanes = 0

for way in waysFile:
    wayCandidate = []
    length = 0
    name = ""
    lanes = 0
    try:
        length = way.d["length"]
    except Exception as e:
        pass
    try:
        for wayTag in way.tag:
            if (wayTag["k"] == "lanes"):
                lanes = wayTag["v"]
            if (wayTag["k"] == "name"):
                name = wayTag["v"]
    except:
        pass

    if length != 0:
        if name != "":
            wayCandidate.append(length)
            wayCandidate.append(name)
            if lanes == 0:
                lanes = 2
                incompleteLanes+=1
            wayCandidate.append(lanes)
    if len(wayCandidate) == 3:
        wayList.append((wayCandidate))
for x in wayList:
    # print(x)
    for y in x:
        print(y)
    print("----")
if incompleteLanes:
    print(str(incompleteLanes) + " ruas no arquivo não possuem informações sobre o número de vias")
    print("Para esses casos assume-se 2 vias (ida e volta)")