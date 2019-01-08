import math
l=set()
 #all possible unique outcomes of a^b
def f():
    for a in xrange(2,101):
        for b in xrange(2,101):
            l.add(a**b)
    return len(l)
print f()

    
