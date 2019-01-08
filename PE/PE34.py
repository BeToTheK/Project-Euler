import math
l=[]

def f(n):
    nxt=0
    s=0
    k=str(n)
    for i in k:
        i=int(i)
        s=math.factorial(int(i))+nxt
        nxt=s
        i+=1
    return nxt


def g():
    for i in range(10,1000000):
        if f(i)==i:
            l.append(i)
        else:
            i+=1
    return sum(l)
print g()
    
        
        
        
    
