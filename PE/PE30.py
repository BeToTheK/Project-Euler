import math
import time
l=[]
def lenstr(n):
    k=len(str(n))
    return k

def s(n):
    i=0
    while i<lenstr(n):
        y=[int(a)**5 for a in str(n)]
        l.append(y)
        i=i+1
        if sum(y)==n:
            return True
        else:
            return False
    return sum(y)
ll=[]
def f():
    i=1
    while lenstr(i)<=5:
        if s(i)==True:
            ll.append(i)
            i=i+1
        else:
            i=i+1
    return ll

print f(),sum(ll)-1
        



