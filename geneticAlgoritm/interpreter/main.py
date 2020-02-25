import importer as i
import aux as a

wayfile, p, pa = i.processInput("output")

pi = a.getSteadyVector(pa)
numVeiculos = 100





densidade = a.getDensidade(wayfile, numVeiculos, pi)

cromossomoInicial = a.getCromossomo(wayfile)

for x in densidade:
    print(x)

print(cromossomoInicial)




#cromossomo é A = [((a,b),(c,d)),((e,f),(g,h))]
#A e o sistema de vias como um todo
#a e e sao ids de rua                             , b e f suas quantidades de vias
#c e g sao os ids de suas respectivas vias opostas, d e h suas quantidades de vias
# ((a,b),(c,d)) é uma unica rua com dois sentidos
