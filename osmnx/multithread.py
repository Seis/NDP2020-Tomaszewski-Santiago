from multiprocessing import Process
import time
import math
import random

def f1(low, up, id2):
    res = 0
    for x in range(low,up):
        res += math.pi*math.e
    # print(graph)
    # print(str(id2) + " " + str(low) + " " + str(up))

u = 1000000000
d = 0
numthreads = 8

listaThread = []

parcela = math.ceil((u-d)/numthreads)


start = time.time()




if __name__ == '__main__':
    print("running in " + str(numthreads) + " threads")

    for x in range(0,numthreads):
        listaThread.append(Process(target=f1, args=(d, parcela, x,)))
        listaThread[-1].start()
        d = d + parcela
        parcela += parcela

    for x in listaThread:
        x.start()

    for x in listaThread:
        x.join()

print("this took " + str(math.ceil(time.time() - start)) + " secs")


# basic

# p = Process(target=f1, args=(d, parcela, x,))
# p.start()
# p.join()
