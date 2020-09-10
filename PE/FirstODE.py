import numpy as np
import math
from sympy import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#y is my hand calc ver.
#using dy(t)/dt=-ky(t)
def y(t,k):
    return exp(-k*t)
l=[]
l1=[]
l2=[]
for i in np.linspace(0,20):
    l2.append(y(i,0.1))
    l1.append(y(i,1))


plt.plot(l1)
plt.plot(l2)
plt.show()

    

