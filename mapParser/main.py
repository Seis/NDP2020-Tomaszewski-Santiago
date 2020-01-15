import untangle
arquivo = untangle.parse("map.osm")
# obj = untangle.parse('path/to/file.xml')
wayList= arquivo.osm.way

for way in wayList:
    for way in way.tag:
        if (way["k"] == "lanes"):
            print(way["v"])
        if (way["k"] == "name"):
            print(way["v"])
            continue