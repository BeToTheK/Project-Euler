import math
import time
start=time.time()

def tri(n):
    return (n**2+n)/2
def pen(n):
    return (3*n**2-n)/2
def hel(n):
    return 2*n**2-n

def triq(t):
    k=(-1+math.sqrt(1+8*t))/2
    if float.is_integer(k):
        return True
    else:
        return False
def penq(p):
    k=(1+math.sqrt(1+24*p))/6
    if float.is_integer(k):
        return True
    else:
        return False
def helq(h):
    k=(1+math.sqrt(1+8*h))/4
    if float.is_integer(k):
        return True
    else:
        return False
l=[]
for i in range(300,1000000):
    k=tri(i)
    if helq(k)==True and penq(k)==True:
        print k
        break
end=time.time()
print end-start
    
