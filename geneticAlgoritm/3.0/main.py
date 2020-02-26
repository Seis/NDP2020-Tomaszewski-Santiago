# coding: U8
import ga
import stringSets




import importer as i
import aux as a


# inicializa numero de geracao
generation = 0

target = 2

def roadGaPrepare(numVeiculos):
    wayfile, p, pa = i.processInput("output")
    pi = a.getSteadyVector(pa)
    densidadeInicial = a.getDensidade(wayfile, numVeiculos, pi)

    cromossomoInicial = a.getCromossomo(wayfile)

    return cromossomoInicial, densidadeInicial,wayfile

def roadGa():
    ancestrais = 




wayfile, p, pa = i.processInput("output")















geneSet = stringSets.enUsSet








# define o objetivo
target="Another head hangs lowly"
# firstParent = ga.generateStandartParent(len(target),' ')

def runGa():
    ancestrais = []
    numeroAncestrais = 10000
    for x in range(0,numeroAncestrais):
        parent = ga.generateParent(len(target), geneSet)
        ancestrais.append(parent)
    return ga.inicialize(geneSet, generation, target, ancestrais)

runGa()

# generationlist = []
# for x in xrange(1,1):
#     generationlist.append(runGa())

# print(generationlist)