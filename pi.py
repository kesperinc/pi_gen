from random import *
def pi_mc(n):
    pi = 0
    count = 0
    for i in range(n):
        x = random()
        y = random()
        if x*x + y*y < 1:
            count += 1
        pi = 4.*float(count) / (i+1)
    return pi


