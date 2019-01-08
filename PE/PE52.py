#It can be seen that the number, 125874,
#and its double, 251748,
#contain exactly the same digits,
#but in a different order.
#Find the smallest positive integer, x
#such that 2x, 3x, 4x, 5x, and 6x,
#contain the same digits.
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
l=[]
def g(n):
    del a[:]
    del b[:]
    del c[:]
    del d[:]
    del e[:]
    del f[:]
    a.append(n)
    b.append(2*n)
    c.append(3*n)
    d.append(4*n)
    e.append(5*n)
    f.append(6*n)
    return

for i in xrange(125800,1000000):
    g(i)
    if list(set(str(a))-set(str(b)))==[] and list(set(str(b))-set(str(a)))==[]:
        if list(set(str(c))-set(str(d)))==[] and list(set(str(d))-set(str(c)))==[]:
            if list(set(str(e))-set(str(f)))==[] and list(set(str(f))-set(str(e)))==[]:
                l.append(i)
                break
    else:
        i+=1
print l        




  
