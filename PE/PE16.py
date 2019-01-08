import math
l=[]
def f(n,p):
    k=tuple(str(n**p))
    return sum(map(int, k))

print f(2,1000)
    


