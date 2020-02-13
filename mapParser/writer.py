import sys
# import argparse
# biblioteca para melhorar os parametros

output_file = sys.argv[2]
input_file = sys.argv[1]

try:
    file = open(output_file, "r")
    print("ERROR!\nOutput file already exists")
    raise IndexError
except (IndexError, IOError) as e:
    try:
        str(input_file)
        str(output_file)
    except IndexError as e:
        print("Usage:\npython " + sys.argv[0] + "input_file output_file")

file = open(output_file, "w")
file.write("23")
file.close()