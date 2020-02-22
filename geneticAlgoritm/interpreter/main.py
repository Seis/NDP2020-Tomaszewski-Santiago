# coding: utf8

import sys
import untangle
import subprocess
import datetime
import io
# import argparse
# biblioteca para melhorar os parametros
print(datetime.datetime.now())



try:
    input_name = sys.argv[1]
    output_name = sys.argv[2]
    output = open(output_name, "r")
    print("ERROR!\nOutput file already exists")
    raise IndexError
except (IndexError, IOError,NameError) as e:
    try:
        str(input_name)
        str(output_name)
    except (IndexError, IOError,NameError) as e:
        print("Usage:\npython " + sys.argv[0] + "i nput_file output_file")
        sys.exit()


pipe = subprocess.Popen(["perl", "osm-length-2-writer.pl", input_name])  # chama o perl que calcula o tamanho das ruas
# print(pipe)
length_file = input_name[:-4] + "_length.osm"


output = io.open(output_name, 'w', encoding='utf8')
# output = open(output_name, "w", encoding='utf8')
xml = untangle.parse(str(length_file))
waysFile = xml.osm.way

wayList = []
incompleteLanesCounter = 0
incompleteOneWaysCounter= 0
laneCounter = 0

print("File pattern")
print("-----------------------------------------------------------------------------")
print("|                                                                           |")
print("| Way section ID                |     1                                     |")
print("| Length of the way section     |     500                                   |")
print("| Lanes in the way section      |     2                                     |")
print("| Transition probabilities      |     (ID1,prob1),(ID2,prob2),(ID3,prob3)   |")
print("|                                                                           |")
print("-----------------------------------------------------------------------------")


for way in waysFile:
    wayCandidate = []
    length = 0
    name = ""
    lanes = 0
    oneway = False
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
            if (wayTag["k"] == "oneway"):
                if wayTag["v"] == "yes":
                    oneway = True
    except:
        pass

    if length != 0:
        if name != "":
            wayCandidate.append(length)
            wayCandidate.append(name)
            if lanes == 0:
                if oneway:
                    lanes = 1
                    incompleteOneWaysCounter += 1
                else:
                    lanes = 2
                incompleteLanesCounter += 1
            wayCandidate.append(lanes)
    if len(wayCandidate) == 3:
        toWrite = ""
        # for x in wayCandidate:
        #     toWrite += str(x) + "\n"
        output.write(way["id"] + "\n")
        output.write(length + "\n")
        output.write(str(lanes) + "\n".decode('unicode-escape'))
        # output.toWrite(name)
        output.write("\n".decode('unicode-escape'))
        laneCounter += 1
output.write(str(laneCounter).decode('unicode-escape'))
output.close()
# for x in wayList:
#     print(x)
#     for y in x:
#         print(y)
#     print("----")
print("There are " + str(laneCounter) + " lanes in the " + str(output_name) + " file.")
if incompleteLanesCounter:
    if incompleteOneWaysCounter:
        print("There are " + str(incompleteLanesCounter) + " streets in the file that don't have the information about the number of ways")
        print("Of these, " + str(incompleteOneWaysCounter) + " ways that have the true on the tag \"oneWay\"")
        print("The program assumes that the street have a single way for them")
        print("For the " + str(incompleteLanesCounter) + " other strets that either don't have the lanes tag neither oneway")
        print("The program assumes that the street have two opposite ways")
    else:
        print("For the " + str(incompleteLanesCounter) + " strets that don't have the lanes tag neither oneway")
        print("The program assumes that the street have two opposite ways")

print(datetime.datetime.now())