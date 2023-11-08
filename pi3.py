from decimal import Decimal
def pi_plauffe(n):
    pi = Decimal(0)
    a,b,c,d = Decimal(4), Decimal(2), Decimal(1), Decimal(1)/Decimal(16)
    for i in range(n):
        i8 = Decimal(8)*i
        pi += (d**i)*(a/(i8+1)-b/(i8+4)-c/(i8+5)-c/(i8+6))
    print(pi)
    return pi

pi_plauffe(300)

