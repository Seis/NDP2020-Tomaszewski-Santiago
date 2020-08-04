import random
import sys

if len(sys.argv) == 2:
    nomeArquivo = sys.argv[1]
    shuffleProbs(nomeArquivo)
else:
    print("randomizer: missing operand")
    print("usage: python3 randomizer.py fileToShuffle")

def randomProbs(totalProb):
    # retorna lista com totalProb probabilidades pseudoaleatorias que somam 100%
    listaProb = []
    total = 1
    while totalProb != 0: 
        if totalProb != 1:
            listaProb.append(round(random.uniform(0,total),2))
            total -= listaProb[-1]
        else:
            listaProb.append(round(total,2))
        totalProb -= 1
        #validacao
        if (totalProb == -1 and sum(listaProb) != 1) or listaProb[-1] < 0.1:
            #refaz sorteio
            totalProb += len(listaProb)
            listaProb = []
            total = 1
        random.shuffle(listaProb)
    return(listaProb)

def shuffleProbs(nomeArquivo):
    listFile = []
    file = open(nomeArquivo, "r")
    for line in file:
        listFile.append(line)
    file.close()

    mapa = []

    for x in range(0,int(len(listFile)),5):
        rua = {}
        rua["id"] = listFile[x].strip()
        rua["comprimento"] = float(listFile[x+1].strip())
        rua["lanes"] = int(listFile[x+2].strip())
        rua["oposta"] = listFile[x+3].strip()
        rua["transicao"] = listFile[x+4].strip().split("|")
        mapa.append(rua)

    for rua in mapa:
        novaTransicao = randomProbs(int(len(rua["transicao"])/2))
        for i in range(1,len(rua["transicao"]),2):
            rua["transicao"][i] = novaTransicao.pop()

    file = open(nomeArquivo + "_shuffled", "x")

    for rua in mapa:
        file.write(str(rua["id"])+"\n")
        file.write(str(rua["comprimento"])+"\n")
        file.write(str(rua["lanes"])+"\n")
        file.write(str(rua["oposta"])+"\n")
        for x in rua["transicao"]:
            file.write(str(x))
            if rua["transicao"][-1] != x:
                file.write("|")
        file.write("\n")