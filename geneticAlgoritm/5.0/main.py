import ga
import time

start = time.time()

ga.run(10000,500,250,"newWayInfo")



time = time.time() - start


print(time)