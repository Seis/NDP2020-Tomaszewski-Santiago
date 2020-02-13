# coding: utf8
import ga

# inicializa numero de geracao
generation = 0
# define os caracteres possiveis
geneSet="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM()'\n "

# define o objetivo
target="Here we are\nDon't turn away now (don't turn away)\nWe are the warriors that built this town\nHere we are\nDon't turn away now (don't turn away)\nWe are the warriors that built this town from dust"

# firstParent = ga.generateStandartParent(len(target),' ')

def runGa():
    ancestrais = []
    numeroAncestrais = 15
    for x in xrange(0,numeroAncestrais):
        parent = ga.generateParent(len(target), geneSet)
        ancestrais.append(parent)
    return ga.inicialize(geneSet, generation, target, ancestrais)

runGa()

# generationlist = []
# for x in xrange(1,1):
#     generationlist.append(runGa())

# print(generationlist)