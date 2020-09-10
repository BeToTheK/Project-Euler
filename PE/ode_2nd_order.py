# load APMonitor package
#from apm import *

# Option 1: solve model with APM MATLAB
#z1 = apm_solve('2nd_order',4)

# Option 2: solve model with ODEINT
from scipy.integrate import odeint
import numpy as np
def model(x,t):
  y = x[0]
  dy = x[1]  
  K = 30
  xdot = [[],[]]
  xdot[0] = dy
  xdot[1] = -(0.9+0.7*t)*dy - K * y
  return xdot
time = np.linspace(0,2,100)
z2 = odeint(model,[2,-1],time)

# plot results
import matplotlib.pyplot as plt
#plt.plot(z1['time'],z1['y'],'r-')
#plt.plot(z1['time'],z1['dy'],'b--')
plt.plot(time,z2[:,0],'g:')
plt.plot(time,z2[:,1],'k-.')
plt.legend(['y (APM Python)','dy/dt (APM Python)','y (ODEINT)','dy/dt (ODEINT)'])
plt.xlabel('Time')
plt.show()
