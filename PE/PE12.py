import math
import time
l=[]
start_time = time.time()
#prints tri number
def next_tri(n):
    k=sum(range(1,n+1))
    return k

def fac(x):
    l=[]
    y = 1
    while y <= math.sqrt(x):
        if x % y == 0:
            l.append(y)
            l.append(int(x / y))
        y += 1
    return len(l)

it=[]
test=[]
def tri(n):
    s=0
    t=0
    for i in range(1,n+1):
        s=i+t
        t=s
        if fac(t)<=500:
            i=i+1
        else:
            it.append(t)
            break
    return it

print tri(100000)
print time.time() - start_time


