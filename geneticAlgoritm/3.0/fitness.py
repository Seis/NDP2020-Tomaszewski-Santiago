import aux

def fitness(cromossomo, matrizOriginal, wayFile, numVeiculos):
	tamanhoCromossomo = len(cromossomo[0])
	xd = cromossomo[1]
	sdvec = []
	for i in range(0,tamanhoCromossomo):
	    sdi = 0
	    if xd[i]:
	        for (j, xdij) in zip(range(0,tamanhoCromossomo), xd):
	            sdi += (matrizOriginal[i][j] * xdij)
	    else:
	        sdi = 1
	    sdvec.append(sdi)
	sd = np.diag(sdvec)
	
    print("-------------------")
    print(matrizOriginal)
    print("-------------------")

	pxd = np.dot(matrizOriginal, xd)
	xdpxd = np.dot(xd, matrizOriginal)

	pcircunflexo = np.dot(sd,xdpxd)



	steadyvector = aux.getSteadyVector(pcircunflexo)
	densidade = aux.getDensidade(wayfile, numVeiculos, steadyvector)

	fitness = max(densidade)

	# return dumbFitness()
	return fitness