import untangle
arquivo = untangle.parse("map.osm")
wayList= arquivo.osm.way


for way in wayList:

    print("a---------------------------------")
    print("e")
    print(way)
    print("b---------------------------------")

    for waya in way.tag:
        if (waya["k"] == "lanes"):
            print(waya["v"])
        if (waya["k"] == "name"):
            print(waya["v"])
            continue
