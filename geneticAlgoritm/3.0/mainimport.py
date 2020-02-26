import importer as i
import aux as a

wayfile, p, pa = i.processInput("output")

pi = a.getSteadyVector(pa)
numVeiculos = 100





densidade = a.getDensidade(wayfile, numVeiculos, pi)

cromossomoInicial = a.getCromossomo(wayfile)






#cromossomo é A = [((a,b),(c,d)),((e,f),(g,h))]
#A e o sistema de vias como um todo
#a e e sao ids de rua                             , b e f suas quantidades de vias
#c e g sao os ids de suas respectivas vias opostas, d e h suas quantidades de vias
# ((a,b),(c,d)) é uma unica rua com dois sentidos



for x in pi:
    print(x)


# 0.06034482758620705
# 0.06034482758620662
# 0.0431034482758621
# 0.04310344827586203
# 0.060344827586206747
# 0.06034482758620718
# 0.10344827586206908
# 0.1034482758620687
# 0.06896551724137921
# 0.06896551724137945
# 0.04310344827586202
# 0.04310344827586215
# 0.06034482758620683
# 0.060344827586206976
# 0.060344827586206976
# 0.06034482758620682

for x in densidade:
    print(x)

# 3.0172413793103527
# 3.017241379310331
# 2.155172413793105
# 2.1551724137931014
# 3.017241379310337
# 3.017241379310359
# 6.896551724137939
# 6.896551724137914
# 6.896551724137921
# 6.896551724137945
# 2.155172413793101
# 2.155172413793107
# 3.0172413793103416
# 3.0172413793103487
# 3.0172413793103487
# 3.017241379310341



print(cromossomoInicial)
# [((1, 2), (2, 2)), ((3, 2), (4, 2)), ((5, 2), (6, 2)), ((7, 1), (8, 1)), ((9, 1), (10, 1)),
# ((11, 2), (12, 2)), ((13, 2), (14, 2)), ((15, 2), (16, 2))]
