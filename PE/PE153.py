l=[]
y=[]
def complexcalc(n):
    count1=0
    count=0
    for a in xrange(1,n+1):
        for b in xrange(0,n+1):
            k=complex(a,b) 
            res=(n/k)
            if res.real.is_integer() and res.imag.is_integer():
                print res
                if res.imag==0:
                    count=res.real+count
                elif res.imag!=0:
                    count1=res.real*2+count1
    return count1+count

print complexcalc(4)
print "space"

