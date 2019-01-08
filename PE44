import math
import time
#Project Euler #44, a bit slow but it works
#my strat was to get a list of all possible values THEN
#search through and find the minimized value BUT
#there was only 1 solution anyway
start = time.time()

#returns Pn
def p(n):
    return n*(3*n-1)/2

#checks if a value 'k' is pent.
##!!this portion does not work well!!##
def checkr(k):
    i=1
    while i<k:
        if p(i)==k:
            return True
        else:
            i+=1
    return False
# Above code is way to slow due to while loop
# must solve for the equation using quadratic eqn'




#function to run the for loop and find pent #'s
def runnr():
    #empty list named l
    l=[]
    #setting up variables
    pentadd=0
    pentmin=0
    for a in xrange(1,5000):
        for b in xrange(a,5000):
            #this is to get around the fact that
            #p(a)-p(b)==0 when a=b
            if a==b:
                pentadd=p(a)+p(b)
            #this gets around that problem
            else:
                pentadd=p(a)+p(b)
                pentmin=p(b)-p(a)
            #figures out sum and difference
            #and checks if they are pent
            test=quadratic(pentadd)
            test1=quadratic(pentmin)
            #if sum==is.pent and if diff.==is.pent
            #append to list named l
            if test==True and test1==True:
                l.append((a,b))
    return l

def quadratic(x):
    a=3
    b=-1
    c=-2*x
    #plus=(-b+math.sqrt(b**2-4*a*c))/2*a
    #minus=(-b-math.sqrt(b**2-4*a*c))/2*a
    plus1=(1+math.sqrt(1+24*x))/6
    #minus1=(1-math.sqrt(1+24*x))/6
    if float.is_integer(plus1):
        return True
    #elif float.is_integer(minus1):
        #return minus1
    else:
        return False

print runnr()
end = time.time()
print (end-start)
#print abs(p(1020)-p(2167))


    
