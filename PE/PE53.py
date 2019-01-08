import math
    #returns n choose r
def c(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
l=[]
    #counts each time c(n,r)>mil.
def f():
    count=0
    for i in xrange(101):
        for j in xrange(i):
            if c(i,j)<=1000000:
                pass
            else:
                count+=1
    return count

print f()


        
        
        
    

    
