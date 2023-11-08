def pi_taylor(n):
    pi = 0.
    for i in range(n):
        pi += 4./float(2.*i+1.)*(-1.)**i
    print(pi)

pi_taylor(3000000)

