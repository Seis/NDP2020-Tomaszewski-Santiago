import subprocess
import sys


input_file = sys.argv[1]
pipe = subprocess.Popen(["perl", "osm-length-2-writer.pl", input_file])