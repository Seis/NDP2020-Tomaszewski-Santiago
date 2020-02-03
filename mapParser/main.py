import untangle
import sys

arquivo = untangle.parse(str(sys.argv[1]))

wayList= arquivo.osm.way

laneList = []
print("Gerando lista para " + str(sys.argv[1]))
for way in wayList:
    lane = []
    try:
        for tag in way.tag:
            if (tag["k"] == "lanes"):
                lane.append(tag["v"])
            if (tag["k"] == "name"):
                lane.append(tag["v"])
            if (len(lane) == 2):
                laneList.append(lane)
                lane = []
                continue
    except:
        pass

print(len(laneList))

for lane in laneList:
    file.write("\n" + str(lane[0]) +  " | " + str(lane[1]))
file.close() 
