import random
import datetime
import time
import os


geneSet="1234567890qwertyuiopasdfghjklzxcvbnmçÇQWERTYUIOPASDFGHJKLZXCVBNM,.@-§áÁéÉóÓãÃõÕêÊẽẼíÍ\n "
target="Tá fazendo mais estrago que ponto 40\nFazendo mais barulho que tiro de oitão\nE nessa boca linda, o cigarro de menta\nVoltou pra casa cedo, quase sem noção"



def generateCleanParent(length): 
    genes = []
    while len(genes) < length:
        genes.extend(' ')
    return ''.join(genes)

def generateParent(length): 
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)

def getFitness(guess):
    correct = 0
    for (expected,atual) in zip(target, guess):
        if expected == atual:
            correct += 1
    return correct

def mutate (parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet,2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return ''.join(childGenes)

def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = getFitness(guess)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("{0}".format(guess))
    # print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

random.seed()
startTime = datetime.datetime.now()
bestParent = generateCleanParent(len(target))
bestFitness = getFitness(bestParent)
display(bestParent)

while True:
    child = mutate(bestParent)
    childFitness = getFitness(child)

    if bestFitness >= childFitness:
        continue
    time.sleep(.05)
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child