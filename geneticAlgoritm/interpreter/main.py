import importer as i
import numpy as np
import math
from scipy import linalg as la
import aux as a

wayfile, p, pa = i.processInput()
length, lanes = i.getLengthLanes(wayfile)

pi = a.getSteadyVector(pa)
nv = 100

densidade = []


   
for (lengthIndividual, laneIndividual , pii) in zip(length, lanes, pi):
    try:
        densidade.append((nv*pii)/(laneIndividual*lengthIndividual))
    except Exception as e:
        densidade.append(0)

cromossomo = a.getCromossomo(wayfile)

for a in densidade:
    print(a)

print(cromossomo)




#cromossomo é A = [((a,b),(c,d)),((e,f),(g,h))]
#A e o sistema de vias como um todo
#a e e sao ids de rua                             , b e f suas quantidades de vias
#c e g sao os ids de suas respectivas vias opostas, d e h suas quantidades de vias
# ((a,b),(c,d)) é uma unica rua com dois sentidos
