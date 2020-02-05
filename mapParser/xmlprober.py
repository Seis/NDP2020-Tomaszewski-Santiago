import sys
f = open(str(sys.argv[1]), 'r')
greaterThan=0
lesserThan=0

for line in f:
    for x in line:
        if x == "<":
            l+=1
        if x == ">":
            g+=1
        if x == "a":
            a+=1
        if x == "b":
            b+=1
        if x == "c":
            c+=1



print(a)
print(b)
print(c)
print(l)
print(g)

f.close()