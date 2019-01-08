def sum_of_sqrs(n):
    s=0
    tot=0
    for i in range(1,n+1):
        s=i**2+tot
        tot=s
        i=i+1
    return tot
def sqr_of_sums(n):
    t=0
    pot=0
    for k in range(1,n+1):
        t=k+pot
        pot=t
        k=k+1
    return pot**2
print sqr_of_sums(100)-sum_of_sqrs(100)

    
