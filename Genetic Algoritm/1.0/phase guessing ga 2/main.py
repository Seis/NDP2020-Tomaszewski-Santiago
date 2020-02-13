import ga

results = []

size = 10
file = open("results for " + str(size) + " predefined ","w") 
file.write("results for " + str(size) + " predefined")

for x in range(1,size):
    results.append(ga.foneoq())
    file.write("\n" + str(x) +  " | " + str(results[-1]))
    if not int(x % 10):
        print(x)

media = 0
for x in results:
    media += x

file.write("\n\n\n\n\n\n")


file.write("\nmedia  " + str(media/size))
file.write("\nminimo " + str(int(min(results))))
file.write("\nmaximo " + str(int(max(results))))
file.close() 