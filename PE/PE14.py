import math
import time
l=[]
start_time = time.time()
def g(n):
    a=0
    b=0
    count=1
    #l.append(n)
    while n>1:
        if n%2==0:
            a=n/2
            n=a
            #l.append(n)
            count=count+1
        else:
            b=3*n+1
            n=b
            #l.append(n)
            count=count+1
    return count

def f():
    a=0
    num=0
    maxx=0
    l=0
    for i in range(1,1000000):
        a=g(i)
        if a>maxx:
            maxx=a
            num=i
            i=i+1
        else:
            i=i+1
    return num

print f()           
            
