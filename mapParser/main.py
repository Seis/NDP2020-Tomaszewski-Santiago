# coding: utf8

import sys
import untangle
import subprocess
import datetime
import io
# import argparse
# biblioteca para melhorar os parametros
print(datetime.datetime.now())
input_name = sys.argv[1]
output_name = sys.argv[2]


try:
    output = open(output_name, "r")
    print("ERROR!\nOutput file already exists")
    raise IndexError
except (IndexError, IOError) as e:
    try:
        str(input_name)
        str(output_name)
    except IndexError as e:
        print("Usage:\npython " + sys.argv[0] + "input_file output_file")


pipe = subprocess.Popen(["perl", "osm-length-2-writer.pl", input_name])  # chama o perl que calcula o tamanho das ruas
# print(pipe)
length_file = input_name[:-4] + "_length.osm"


output = io.open(output_name, 'w', encoding='utf8')
# output = open(output_name, "w", encoding='utf8')
xml = untangle.parse(str(length_file))
waysFile = xml.osm.way

wayList = []
incompleteLanesCounter = 0
laneCounter = 0

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
                incompleteLanesCounter+=1
            wayCandidate.append(lanes)
    if len(wayCandidate) == 3:
        toWrite = ""
        # for x in wayCandidate:
        #     toWrite += str(x) + "\n"

        toWrite = way["id"] + " || " + str(length) + " || " + str(lanes) +  " || " + name +  "\n"
        laneCounter += 1








        output.write(toWrite)
        # wayList.append((wayCandidate))
output.write(str(laneCounter).decode('unicode-escape'))
output.close()
# for x in wayList:
#     print(x)
#     for y in x:
#         print(y)
#     print("----")
print("There are " + str(laneCounter) + " lanes in the " + str(output_name) + " file.")
if incompleteLanesCounter:
    print("There are " + str(incompleteLanesCounter) + " streets in the file that don't have the information about the number of ways")
    print("In this cases the program assumes that the street have 2 opossite ways")

print(datetime.datetime.now())