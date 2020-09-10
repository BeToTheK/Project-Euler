import numpy as np
import matplotlib.pyplot as plt
a=[]
b=[]
na=-1*[]
nb=-1*[]
Y=[]
#itterates z_n+1=zn^2+c where c ranges
#from -2,2 with increments of 1/500
#ten times or n(while statement)
def f(c):
    i=0
    z0=complex(0)
    while i<10:
        zn=z0**2+c
        new=zn
        z0=new
        absl=abs(new)
        if absl<=2:
            i+=1
        else:
            return False
    return True

for i in np.linspace(-2,2,num=300):
    for j in np.linspace(-2,2,num=300):
        c=complex(i,j)
        if f(c)==True:
            a.append(i)
            b.append(j)

plt.scatter(a,b,s=5)
plt.show()

#counts number of itterations
aa=[]
bb=[]
l=[]
def g(c):
    i=0
    count=0
    z0=complex(0)
    while i<10:
        zn=z0**2+c
        new=zn
        z0=new
        absl=abs(new)
        if absl<=2:
            i+=1
            count+=1
        else:
            return count
    return 0

for i in np.linspace(-2,2,num=30):
    for j in np.linspace(-2,2,num=30):
        c=complex(i,j)
        if g(c)>0:
            l.append(g(c))
            
        
#plt.plot(l)
#plt.show()
            
