import untangle
arquivo = untangle.parse("mapaponte_lenght.osm")
waysFile = arquivo.osm.way


wayList = []
wayCandidate = []

for way in waysFile:
    try:
        wayCandidate.append(way.d["length"])
    except Exception as e:
        pass
    for wayTag in way.tag:
        if (wayTag["k"] == "lanes"):
            wayCandidate.append(wayTag["v"])
        if (wayTag["k"] == "name"):
            wayCandidate.append(wayTag["v"])
    if len(wayCandidate) == 3:
        wayList.append(wayCandidate)
        print(wayCandidate)
    else:
        for x in wayCandidate:
            print(wayCandidate)
    wayCandidate = []

print(len(wayList))
