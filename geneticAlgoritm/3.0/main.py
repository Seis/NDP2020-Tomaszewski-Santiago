# coding: U8
import ga
import stringSets
# enUsSet
# fullSet

# isoSet = "qwertyuiopasdfghjklzxcvbnm"
# capitalIsoSet = "QWERTYUIOPASDFGHJKLZXCVBNM"
# numberSet = "1234567890"
# acentSet = "áéíóúãẽõĩũâêîôûàèìòùç"
# capitalAcentSet = "ÁÉÍÓÚÃẼĨÕŨÂÊÎÔÛÀÈÌÒÙÇ"
# specialSet = "',.?()!-\n "
# superSpecialSet = ";<>:/\|[]{}=+_*&$$#@"

# enUsSet = isoSet + capitalIsoSet + numberSet + specialSet
# fullSet = isoSet + capitalIsoSet + numberSet + acentSet + capitalAcentSet + specialSet + superSpecialSet

# inicializa numero de geracao
generation = 0
# define os caracteres possiveis

geneSet = stringSets.enUsSet








# define o objetivo
target="Another head hangs lowly"
# firstParent = ga.generateStandartParent(len(target),' ')

def runGa():
    ancestrais = []
    numeroAncestrais = 10000
    for x in xrange(0,numeroAncestrais):
        parent = ga.generateParent(len(target), geneSet)
        ancestrais.append(parent)
    return ga.inicialize(geneSet, generation, target, ancestrais)

runGa()

# generationlist = []
# for x in xrange(1,1):
#     generationlist.append(runGa())

# print(generationlist)