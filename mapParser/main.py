import sys
import untangle
arquivo = untangle.parse(str(sys.argv[1]))
#arquivo = untangle.parse("newPonteLenght.osm")
print("parsing")
waysFile = arquivo.osm.way


wayList = [[]]
wayCandidate = []

for way in waysFile:
    try:
        wayCandidate.append(way.d["length"])
    except Exception as e:
        pass

    try:
        for wayTag in way.tag:
            # if (wayTag["k"] == "lanes"):
                # wayCandidate.append(wayTag["v"])
            if (wayTag["k"] == "name"):
                wayCandidate.append(wayTag["v"])
    except:
        pass
    if len(wayCandidate) == 2:
        wayList.append(wayCandidate)
    wayCandidate = []
for x in wayList:
    for y in x:
        print(y)
    print("----")